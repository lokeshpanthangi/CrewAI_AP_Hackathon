# 🚔 IPDR Police Investigation Platform

> **A comprehensive AI-powered investigation platform for law enforcement agencies to analyze Call Detail Records (CDR), Internet Protocol Detail Records (IPDR), and other telecommunications data with advanced graph database integration and intelligent query processing.**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![React](https://img.shields.io/badge/React-18+-61DAFB.svg)](https://reactjs.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-Latest-009688.svg)](https://fastapi.tiangolo.com)
[![Neo4j](https://img.shields.io/badge/Neo4j-5.x-008CC1.svg)](https://neo4j.com)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-412991.svg)](https://openai.com)

## 🌟 Overview

The IPDR Police Investigation Platform is a cutting-edge solution designed specifically for law enforcement agencies to conduct sophisticated telecommunications data analysis. It combines the power of AI, graph databases, and modern web technologies to provide investigators with unprecedented insights into communication patterns, network relationships, and suspicious activities.

### 🎯 Key Features

- 🤖 **AI-Powered Analysis**: GPT-4 integration for intelligent query processing and pattern recognition
- 🕸️ **Graph Database**: Neo4j integration for complex relationship mapping and network analysis
- 📊 **Multi-Format Support**: Process CDR, IPDR, SMS, bank records, and more
- 🔍 **Smart Query Interface**: Natural language to Cypher query conversion
- 📈 **Real-time Analytics**: Interactive dashboards and visualization tools
- 🔐 **Secure Architecture**: Environment-based configuration and secure API handling
- 📱 **Modern UI**: Responsive React-based interface with intuitive navigation
- 🚀 **Agentic System**: Intelligent investigation agents for automated analysis

## 🏗️ Architecture

```
🌐 Frontend (React + Vite)
    ├── 📱 Chat Interface (Natural Language Queries)
    ├── 📊 Dashboard (Analytics & Visualizations)
    ├── 📁 File Management (Upload & Processing)
    ├── 📋 Reports (Investigation Summaries)
    └── ⚙️ Settings (Configuration)
            ↓
🔗 API Layer (FastAPI)
    ├── 🤖 Agentic API (AI Investigation Agents)
    ├── 📄 PDF Chat (Document Analysis)
    ├── 📊 File Processing (Data Extraction)
    └── 🗄️ Database Operations
            ↓
💾 Data Layer
    ├── 🕸️ Neo4j (Graph Database - Relationships)
    ├── 🗃️ Supabase (PostgreSQL - Structured Data)
    └── 🤖 OpenAI (GPT-4 - AI Processing)
```

## 🚀 Quick Start

### 📋 Prerequisites

- 🐍 Python 3.8 or higher
- 📦 Node.js 16 or higher
- 🔑 OpenAI API key
- 🗄️ Supabase account (optional)
- 🕸️ Neo4j database (optional)

### ⚡ Installation

1. **📥 Clone the Repository**
```bash
git clone <repository-url>
cd ContentMissingorUnspecified
```

2. **🔧 Environment Setup**
```bash
# Copy and configure environment variables
cp .env.example .env
# Edit .env with your API keys
```

3. **🐍 Python Dependencies**
```bash
pip install -r requirements.txt
```

4. **📦 Node.js Dependencies**
```bash
npm install
```

5. **🚀 Start the Application**
```bash
# Start all servers
python start_servers.py

# Or start individually:
# Backend API
python api_server.py

# Agentic System
python agentic_api.py

# Frontend (in separate terminal)
npm run dev
```

## 🔧 Configuration

### 🌍 Environment Variables

Create a `.env` file in the root directory:

```env
# 🤖 OpenAI Configuration
VITE_OPENAI_API_KEY=your_openai_api_key_here

# 🕸️ Neo4j Configuration
NEO4J_URI=neo4j+s://your-neo4j-instance.databases.neo4j.io
NEO4J_USER=neo4j
NEO4J_PASSWORD=your_neo4j_password
NEXT_NEO4J_USERNAME=neo4j
NEXT_NEO4J_PASSWORD=your_neo4j_password

# 🗃️ Supabase Configuration
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_ANON_KEY=your_supabase_anon_key
```

### 🔑 API Keys Setup

#### OpenAI API Key
1. 🌐 Visit [OpenAI Platform](https://platform.openai.com/api-keys)
2. 🔐 Create a new API key
3. 💰 Ensure your account has sufficient credits
4. 📝 Add the key to your `.env` file

#### Neo4j Database
1. 🌐 Visit [Neo4j AuraDB](https://neo4j.com/cloud/aura/)
2. 🆕 Create a new database instance
3. 📝 Note the connection URI and credentials
4. 🔧 Update your `.env` file

#### Supabase Database
1. 🌐 Visit [Supabase](https://supabase.com)
2. 🆕 Create a new project
3. 🔑 Get your project URL and anon key
4. 📝 Update your `.env` file

## 💼 Usage

### 🎯 Main Investigation Interface

1. **🚀 Start the Application**
```bash
python start_servers.py
```

2. **🌐 Open Your Browser**
   - Navigate to `http://localhost:5173`
   - Access the investigation dashboard

3. **💬 Natural Language Queries**
   - Ask questions like: "Show me all calls between these numbers"
   - "Find suspicious communication patterns"
   - "Analyze network connections for this IMEI"

### 📊 File Processing

#### 📁 Supported File Types

- 📞 **CDR Files**: Call Detail Records (.csv, .xlsx)
- 🌐 **IPDR Files**: Internet Protocol Detail Records (.json, .csv)
- 💬 **SMS Data**: SMS header and content files
- 🏦 **Bank Records**: Transaction data (.csv, .xlsx)
- 🗼 **Tower Dumps**: Cell tower data (.csv)
- 📄 **PDF Documents**: Interactive chat with GPT-4
- 📝 **Word Documents**: Table extraction and analysis

#### 🔄 Processing Workflow

```
📁 File Upload
    ↓
🔍 Automatic Schema Detection
    ↓
✅ Data Validation
    ↓
📋 Preview & Confirmation
    ↓
💾 Database Insertion
    ↓
📊 Analysis Ready
```

### 🤖 Agentic Investigation System

The platform includes intelligent investigation agents:

- 🕵️ **Pattern Analysis Agent**: Identifies suspicious communication patterns
- 🌐 **Network Mapping Agent**: Creates relationship graphs
- 📊 **Data Correlation Agent**: Finds connections across datasets
- 📝 **Report Generation Agent**: Creates comprehensive investigation reports

## 📊 Data Models

### 🗄️ Supported Database Tables

| Table | Description | Key Fields |
|-------|-------------|------------|
| 📞 `crd` | Call Detail Records | a_party, b_party, date, duration |
| 🌐 `ipdr` | Internet Protocol Records | user_id, ip_address, timestamp |
| 💬 `sms_header` | SMS Header Information | sender, receiver, timestamp |
| 🏦 `bank_details` | Bank Transaction Data | ac_no, tran_date, amount |
| 🗼 `tower_dumps` | Cell Tower Data | cell_id, location, timestamp |
| 📱 `true_caller` | True Caller Database | phone_number, name, location |

### 🕸️ Graph Database Schema

Neo4j stores relationships between:
- 📱 Phone numbers and their connections
- 🌐 IP addresses and user activities
- 🗼 Cell towers and device locations
- 🏦 Financial transactions and accounts

## 🔍 Advanced Features

### 🧠 AI-Powered Query Processing

```python
# Natural language input
"Find all calls longer than 30 minutes between Mumbai and Delhi"

# Automatically converts to Cypher
MATCH (a:Phone)-[c:CALLED]->(b:Phone)
WHERE c.duration > 1800 
AND a.location = 'Mumbai' 
AND b.location = 'Delhi'
RETURN a, c, b
```

### 📈 Real-time Analytics

- 📊 **Communication Frequency**: Call/SMS patterns over time
- 🌍 **Geographic Analysis**: Location-based activity mapping
- 🕰️ **Temporal Patterns**: Time-based behavior analysis
- 🔗 **Network Analysis**: Relationship strength and centrality

### 🔐 Security Features

- 🔒 **Environment-based Configuration**: No hardcoded credentials
- 🛡️ **API Key Rotation**: Support for key management
- 🔐 **Secure Database Connections**: Encrypted connections to all databases
- 📝 **Audit Logging**: Complete investigation trail

## 🛠️ Development

### 📁 Project Structure

```
📦 IPDR Police Investigation Platform
├── 🐍 Backend (Python)
│   ├── 🚀 api_server.py          # Main API server
│   ├── 🤖 agentic_api.py         # AI investigation agents
│   ├── 📄 pdf_chat.py            # PDF document analysis
│   ├── 📊 files.py               # File processing
│   ├── 🗄️ supabase_handler.py    # Database operations
│   ├── 🔧 config.py              # Configuration
│   └── 📋 requirements.txt       # Python dependencies
├── 🌐 Frontend (React)
│   ├── 📱 src/pages/             # Application pages
│   ├── 🧩 src/components/        # Reusable components
│   ├── 🔧 src/services/          # API services
│   ├── 🛠️ src/utils/             # Utility functions
│   └── 📦 package.json           # Node.js dependencies
├── 🔧 Configuration
│   ├── 🌍 .env                   # Environment variables
│   ├── ⚙️ vite.config.js         # Vite configuration
│   └── 🎨 tailwind.config.js     # Tailwind CSS config
└── 📚 Documentation
    ├── 📖 README.md              # This file
    ├── 🔧 SETUP_GUIDE.md         # Detailed setup guide
    └── 📋 API_DOCUMENTATION.md   # API reference
```

### 🔧 Adding New Features

#### 📊 Adding New Data Types

1. **Update Schema Configuration**
```python
# In config.py
TABLE_SCHEMAS["new_table"] = {
    "required_columns": ["col1", "col2"],
    "column_types": {"col1": "text", "col2": "integer"},
    "keywords": ["keyword1", "keyword2"]
}
```

2. **Add Processing Logic**
```python
# In files.py
def process_new_data_type(file_path):
    # Custom processing logic
    pass
```

#### 🤖 Creating New Investigation Agents

```python
# In src/services/investigationAgents.js
export const newAnalysisAgent = async (data) => {
    const prompt = "Analyze this data for...";
    return await callOpenAI(prompt, data);
};
```

## 🚨 Troubleshooting

### ❌ Common Issues

#### 🔑 API Key Issues
```bash
❌ OpenAI API Error: Invalid API key
✅ Solution: Check your .env file and ensure VITE_OPENAI_API_KEY is set
```

#### 🗄️ Database Connection Issues
```bash
❌ Neo4j Connection Failed
✅ Solution: Verify NEO4J_URI, NEO4J_USER, and NEO4J_PASSWORD in .env
```

#### 📦 Module Import Errors
```bash
❌ ModuleNotFoundError: No module named 'openai'
✅ Solution: Run 'pip install -r requirements.txt'
```

### 🔧 Debug Mode

```bash
# Enable debug logging
export DEBUG=true
python api_server.py
```

## 📈 Performance Optimization

### 🚀 Recommended Settings

- **🧠 Memory**: Minimum 8GB RAM for large datasets
- **💾 Storage**: SSD recommended for database operations
- **🌐 Network**: Stable internet for AI API calls
- **🔧 Batch Size**: Adjust batch processing size based on available memory

### 📊 Monitoring

- 📈 **API Response Times**: Monitor OpenAI API latency
- 🗄️ **Database Performance**: Track Neo4j and Supabase query times
- 💾 **Memory Usage**: Monitor Python process memory consumption
- 🌐 **Network Usage**: Track API call frequency and data transfer

## 🤝 Contributing

1. 🍴 Fork the repository
2. 🌿 Create a feature branch (`git checkout -b feature/amazing-feature`)
3. 💾 Commit your changes (`git commit -m 'Add amazing feature'`)
4. 📤 Push to the branch (`git push origin feature/amazing-feature`)
5. 🔄 Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- 🤖 **OpenAI** for GPT-4 API
- 🕸️ **Neo4j** for graph database technology
- 🗃️ **Supabase** for PostgreSQL hosting
- ⚛️ **React Team** for the frontend framework
- 🚀 **FastAPI** for the backend framework

## 📞 Support

For support and questions:
- 📧 Email: support@investigation-platform.com
- 💬 Discord: [Join our community](https://discord.gg/investigation-platform)
- 📖 Documentation: [Full documentation](https://docs.investigation-platform.com)
- 🐛 Issues: [GitHub Issues](https://github.com/your-repo/issues)

---

**⚠️ Important Notice**: This platform is designed for legitimate law enforcement use only. Ensure compliance with local laws and regulations regarding data privacy and surveillance.

**🔐 Security**: Always use environment variables for sensitive configuration. Never commit API keys or credentials to version control.

**📊 Data Privacy**: Implement proper data handling procedures and ensure compliance with relevant privacy regulations in your jurisdiction.

---

*Made with ❤️ for law enforcement professionals worldwide* 🌍