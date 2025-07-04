#!/usr/bin/env python3
"""
Agentic Investigation Platform - Server Startup Script
Starts all necessary servers for the agentic investigation system
"""

import subprocess
import sys
import time
import os
import signal
from concurrent.futures import ThreadPoolExecutor
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ServerManager:
    def __init__(self):
        self.processes = []
        self.executor = ThreadPoolExecutor(max_workers=5)
        
    def start_server(self, name, command, cwd=None, env=None):
        """Start a server process"""
        logger.info(f"🚀 Starting {name}...")
        
        try:
            # Prepare environment
            server_env = os.environ.copy()
            if env:
                server_env.update(env)
            
            # Start the process
            process = subprocess.Popen(
                command,
                shell=True,
                cwd=cwd,
                env=server_env,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
                bufsize=1
            )
            
            self.processes.append({
                'name': name,
                'process': process,
                'command': command
            })
            
            logger.info(f"✅ {name} started with PID: {process.pid}")
            
            # Monitor output
            def monitor_output():
                try:
                    for line in iter(process.stdout.readline, ''):
                        if line:
                            print(f"[{name}] {line.strip()}")
                    process.stdout.close()
                except Exception as e:
                    logger.error(f"❌ Error monitoring {name}: {e}")
            
            self.executor.submit(monitor_output)
            
            return process
            
        except Exception as e:
            logger.error(f"❌ Failed to start {name}: {e}")
            return None
    
    def stop_all_servers(self):
        """Stop all running servers"""
        logger.info("🛑 Stopping all servers...")
        
        for server in self.processes:
            try:
                name = server['name']
                process = server['process']
                
                if process.poll() is None:  # Process is still running
                    logger.info(f"🛑 Stopping {name} (PID: {process.pid})...")
                    
                    # Try graceful shutdown first
                    process.terminate()
                    
                    # Wait for graceful shutdown
                    try:
                        process.wait(timeout=5)
                        logger.info(f"✅ {name} stopped gracefully")
                    except subprocess.TimeoutExpired:
                        # Force kill if graceful shutdown fails
                        logger.warning(f"⚡ Force killing {name}...")
                        process.kill()
                        process.wait()
                        logger.info(f"✅ {name} force stopped")
                        
            except Exception as e:
                logger.error(f"❌ Error stopping {server['name']}: {e}")
        
        self.executor.shutdown(wait=True)
        logger.info("✅ All servers stopped")
    
    def check_dependencies(self):
        """Check if all required dependencies are available"""
        logger.info("🔍 Checking dependencies...")
        
        dependencies = [
            ("python", "Python interpreter"),
            ("node", "Node.js"),
            ("npm", "NPM package manager")
        ]
        
        missing = []
        for cmd, desc in dependencies:
            try:
                subprocess.run([cmd, "--version"], 
                             capture_output=True, 
                             check=True)
                logger.info(f"✅ {desc} is available")
            except (subprocess.CalledProcessError, FileNotFoundError):
                logger.error(f"❌ {desc} is missing")
                missing.append(desc)
        
        if missing:
            logger.error(f"❌ Missing dependencies: {', '.join(missing)}")
            return False
        
        logger.info("✅ All dependencies are available")
        return True
    
    def install_python_dependencies(self):
        """Install Python dependencies"""
        logger.info("📦 Installing Python dependencies...")
        
        try:
            subprocess.run([
                sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
            ], check=True)
            logger.info("✅ Python dependencies installed")
            return True
        except subprocess.CalledProcessError as e:
            logger.error(f"❌ Failed to install Python dependencies: {e}")
            return False
    
    def install_node_dependencies(self):
        """Install Node.js dependencies"""
        logger.info("📦 Installing Node.js dependencies...")
        
        try:
            subprocess.run(["npm", "install"], check=True)
            logger.info("✅ Node.js dependencies installed")
            return True
        except subprocess.CalledProcessError as e:
            logger.error(f"❌ Failed to install Node.js dependencies: {e}")
            return False

def main():
    """Main function to start all servers"""
    
    print("🎯 AGENTIC INVESTIGATION PLATFORM")
    print("=" * 50)
    print("🚀 Starting all servers for the investigation platform...")
    print()
    
    manager = ServerManager()
    
    def signal_handler(signum, frame):
        print("\n🛑 Received shutdown signal...")
        manager.stop_all_servers()
        sys.exit(0)
    
    # Register signal handlers
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    try:
        # Check dependencies
        if not manager.check_dependencies():
            logger.error("❌ Dependency check failed. Please install missing dependencies.")
            return 1
        
        # Install dependencies
        print("📦 Installing dependencies...")
        if not manager.install_python_dependencies():
            logger.error("❌ Failed to install Python dependencies")
            return 1
        
        if not manager.install_node_dependencies():
            logger.error("❌ Failed to install Node.js dependencies")
            return 1
        
        print("\n🚀 Starting servers...")
        print("-" * 30)
        
        # Start Agentic API Server (Port 8001)
        manager.start_server(
            name="Agentic API",
            command="python -m uvicorn agentic_api:app --host 0.0.0.0 --port 8001 --reload",
            cwd="."
        )
        
        # Wait a bit for the API server to start
        time.sleep(2)
        
        # Start Main API Server (Port 8000)
        manager.start_server(
            name="Main API",
            command="python api_server.py",
            cwd="."
        )
        
        # Wait a bit for the main API to start
        time.sleep(2)
        
        # Start Frontend Development Server (Port 5173)
        manager.start_server(
            name="Frontend",
            command="npm run dev",
            cwd="."
        )
        
        # Wait a bit for frontend to start
        time.sleep(3)
        
        print("\n" + "=" * 50)
        print("🎉 ALL SERVERS STARTED SUCCESSFULLY!")
        print("=" * 50)
        print()
        print("📍 Server URLs:")
        print("   🌐 Frontend:     http://localhost:5173")
        print("   🤖 Agentic API:  http://localhost:8001")
        print("   📊 Main API:     http://localhost:8000")
        print()
        print("📋 Available Endpoints:")
        print("   🧠 Agentic Chat: http://localhost:8001/api/investigate")
        print("   📊 Health Check: http://localhost:8001/api/health")
        print("   📖 API Docs:     http://localhost:8001/docs")
        print()
        print("🔧 Usage:")
        print("   1. Open http://localhost:5173 in your browser")
        print("   2. Navigate to the Chat section")
        print("   3. Start asking investigation questions!")
        print()
        print("💡 Example Queries:")
        print("   • 'Analyze phone number 9876543210 for suspicious activity'")
        print("   • 'Track internet usage for user ID 12345 last week'")
        print("   • 'Find movement patterns between Mumbai and Delhi'")
        print()
        print("Press Ctrl+C to stop all servers")
        print("-" * 50)
        
        # Keep the main thread alive
        while True:
            time.sleep(1)
            
            # Check if any process has died
            for server in manager.processes:
                if server['process'].poll() is not None:
                    logger.warning(f"⚠️ {server['name']} has stopped unexpectedly")
                    # Optionally restart the server
                    # manager.start_server(server['name'], server['command'])
                    
    except KeyboardInterrupt:
        print("\n🛑 Keyboard interrupt received...")
    except Exception as e:
        logger.error(f"❌ Unexpected error: {e}")
        return 1
    finally:
        manager.stop_all_servers()
    
    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code) 