<p align="center">
  <img src="https://raw.githubusercontent.com/getbindu/create-bindu-agent/refs/heads/main/assets/light.svg" alt="bindu Logo" width="200">
</p>

<h1 align="center">documentation-generator</h1>
<h3 align="center">The README Generator Agent is an intelligent automation tool that creates comprehensive, professional README files for open source projects. This agent leverages the power of AI to analyze GitHub repositories and generate well-structured documentation automatically.</h3>

<p align="center">
  <strong>The README Generator Agent is an intelligent automation tool that creates comprehensive, professional README files for open source projects. This agent leverages the power of AI to analyze GitHub repositories and generate well-structured documentation automatically.</strong><br/>
  The README Generator Agent is an intelligent automation tool that creates comprehensive, professional README files for open source projects. This agent leverages the power of AI to analyze GitHub repositories and generate well-structured documentation automatically.
</p>

<p align="center">
  <a href="https://github.com/lsvishaal/documentation-generator/actions/workflows/main.yml?query=branch%3Amain">
    <img src="https://img.shields.io/github/actions/workflow/status/lsvishaal/documentation-generator/main.yml?branch=main" alt="Build status">
  </a>
  <a href="https://codecov.io/gh/lsvishaal/documentation-generator">
    <img src="https://codecov.io/gh/lsvishaal/documentation-generator/branch/main/graph/badge.svg" alt="codecov">
  </a>
  <a href="https://img.shields.io/github/license/lsvishaal/documentation-generator">
    <img src="https://img.shields.io/github/license/lsvishaal/documentation-generator" alt="License">
  </a>
</p>

---

## 💡 Why This Exists

**Stop endless scrolling.** This AI agent understands what you *actually* want:

**Perfect for:** The README Generator Agent is an intelligent automation tool that creates comprehensive, professional README files for open source projects. This agent leverages the power of AI to analyze GitHub repositories and generate well-structured documentation automatically.

---

> **🌐 Join the Internet of Agents**  
> Register your agent at [bindus.directory](https://bindus.directory) to make it discoverable worldwide and enable agent-to-agent collaboration. **It takes 2 minutes and unlocks the full potential of your agent.**

---

## 📚 Quick Links

- 📖 **[Full Documentation](https://lsvishaal.github.io/documentation-generator/)**
- 💻 **[GitHub Repository](https://github.com/lsvishaal/documentation-generator/)**
- 🐛 **[Report Issues](https://github.com/lsvishaal/documentation-generator/issues)**
- 💬 **[Join Discord](https://discord.gg/3w5zuYUuwt)**
- 🌐 **[Agent Directory](https://bindus.directory)**

<br/>

## ⚡ Quick Start - Deploy to bindus.directory in 5 Minutes

This guide will help you deploy your agent to [bindus.directory](https://bindus.directory) where it becomes discoverable worldwide and can collaborate with other agents. **GitHub Actions will automatically build, containerize, and register your agent.**

### Prerequisites

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) (fast Python package installer)
- [GitHub CLI](https://cli.github.com/) (`gh`)
- GitHub account
- Docker Hub account (free)

---

### 1️⃣ Local Setup & Configuration

```bash
# Clone and setup the project
cd documentation-generator
uv venv --python 3.12.9
source .venv/bin/activate
uv sync

# Configure API keys
cp .env.example .env
```

Edit `.env` and add your keys:

| Key | Get It From | Free Tier? |
|-----|-------------|------------|
| `OPENROUTER_API_KEY` | [OpenRouter](https://openrouter.ai/keys) | ✅ Yes |
| `MEM0_API_KEY` | [Mem0 Dashboard](https://app.mem0.ai/dashboard/api-keys) | ✅ Yes |

---

### 2️⃣ Setup GitHub Authentication

Authenticate with GitHub CLI:

```bash
# Check if you're already logged in
gh auth status

# If not logged in, authenticate with GitHub
gh auth login
```

Follow the prompts:
1. Select **GitHub.com**
2. Choose **SSH** as your preferred protocol
3. Authenticate via your browser or token

---

### 3️⃣ Create GitHub Repository

# Initialize git repository and commit your code
git init -b main
git add .
git commit -m "Initial commit"

# Create repository on GitHub and push (replace with your GitHub username)
gh repo create lsvishaal/documentation-generator --public --source=. --remote=origin --push
```

**Alternative: Manual creation**
1. Create repository at https://github.com/new
2. Don't initialize with README (you already have one)
3. Then run:
```bash
git remote add origin https://github.com/lsvishaal/documentation-generator.git
git push -u origin main

---

### 4️⃣ Register on bindus.directory

1. **Login** to [bindus.directory](https://bindus.directory)
2. **Grab your API key** from the dashboard
3. **Get Docker Hub token** from [Docker Hub Security Settings](https://hub.docker.com/settings/security)

---

### 5️⃣ Configure GitHub Secrets for Auto-Deployment

Set up secrets so GitHub Actions can automatically deploy your agent:

![GitHub Secrets Setup](../assets/git_secret.png)

```bash
gh secret set BINDU_API_TOKEN --body "<your-bindus-api-key>"
gh secret set DOCKERHUB_TOKEN --body "<your-dockerhub-token>"
```

---

### 6️⃣ Deploy! 🚀

**Push to trigger automatic deployment:**

```bash
git push origin main
```

**What happens automatically:**
1. ✅ GitHub Actions builds your agent
2. ✅ Creates a Docker container
3. ✅ Pushes to Docker Hub
4. ✅ Registers on bindus.directory
5. ✅ Your agent is now live and discoverable!

**That's it!** 🎉 Your agent is now part of the Internet of Agents.

---

## � Sample Output

### Example: torvalds/linux README

Here's an actual README generated by this agent for the Linux kernel:

```markdown
# Linux Kernel

![License](https://img.shields.io/badge/license-Other-blue.svg) ![Stars](https://img.shields.io/github/stars/torvalds/linux.svg) ![Forks](https://img.shields.io/github/forks/torvalds/linux.svg) ![Open Issues](https://img.shields.io/github/issues/torvalds/linux.svg) ![Release](https://img.shields.io/github/v/release/torvalds/linux.svg) ![Repo Size](https://img.shields.io/github/repo-size/torvalds/linux.svg)

## Description
The Linux kernel source tree.

## Cloning the Repository

\`\`\`bash
git clone https://github.com/torvalds/linux.git
\`\`\`

## Installation

Before compiling the Linux kernel, ensure you have all the dependencies installed.

\`\`\`bash
cd linux
make menuconfig  # To configure the kernel options
make                # To compile the kernel
sudo make modules_install
sudo make install   # To install the kernel
\`\`\`

## Contributing

Contributions are welcome! Please read the contributing guidelines and follow best practices for submitting patches.
\`\`\`

### Key Features of Generated READMEs

✅ Automated badge generation (stars, forks, issues, license)  
✅ Clone and installation instructions  
✅ Usage examples  
✅ Development contribution guidelines  
✅ Resource links and documentation references  
✅ Professional, maintainer-friendly structure

---

## 🛠️ Development Setup

### Running Tests

```bash
make test              # Run all tests
make test-cov          # With coverage report
```

### Code Quality

```bash
make format            # Format code
make lint              # Run linters
make check             # Format + lint + test
```

### Pre-commit Hooks

Fix formatting issues before committing:

```bash
uv run pre-commit run -a
```

---

## 🐳 Docker Deployment & Bindu Directory Registration

### Understanding Your Tokens

To deploy your agent to the Bindu directory (bindus.directory), you need **two tokens**:

#### 1. **BINDU_API_TOKEN** (Bindu Directory Authentication)

**What it is**: Authentication token from the Bindu directory for agent registration and discovery  
**Where to get it**:
1. Visit https://bindus.directory
2. Sign in (create free account if needed)
3. Go to your dashboard/settings
4. Copy your API token (labeled as `BINDU_PAT_TOKEN`)

**Purpose**: Makes your agent discoverable worldwide in bindus.directory for agent-to-agent collaboration

#### 2. **DOCKERHUB_TOKEN** (Docker Registry Authentication)

**What it is**: Personal access token for pushing Docker images to Docker Hub  
**Where to get it**:
1. Visit https://hub.docker.com/settings/security
2. Click "New Access Token"
3. Name it: "documentation-generator"
4. Select "Read & Write" permissions
5. Copy token immediately (visible only once)

**Purpose**: Allows GitHub Actions to automatically push your Docker image to Docker Hub

### Local Docker Setup

```bash
# Build and run locally
docker-compose up --build

# Production mode (with optimizations)
docker-compose -f docker-compose.prod.yml up
```

### Automatic Deployment to Bindu Directory

**Step 1: Add GitHub Secrets**

```bash
# Add Bindu directory token
gh secret set BINDU_API_TOKEN --body "<your-bindu-token-here>"

# Add Docker Hub token  
gh secret set DOCKERHUB_TOKEN --body "<your-docker-token-here>"

# Add Docker Hub username
gh secret set DOCKERHUB_USERNAME --body "<your-docker-username>"
```

**Step 2: Push to Trigger Deployment**

```bash
git push origin main
```

**Step 3: Automatic Actions**

GitHub Actions will automatically:
1. ✅ Build your agent Docker image
2. ✅ Push it to Docker Hub  
3. ✅ Register your agent in bindus.directory
4. ✅ Make it discoverable to other agents worldwide

**Step 4: Verify Registration**

1. Visit https://bindus.directory
2. Search for your agent by name
3. Your agent card appears with full metadata

---

## 🏗️ Project Structure

```
documentation-generator/
├── documentation_generator/    # Main agent code
│   ├── skills/             # Agent capabilities
│   │   └── documentation_generator/ # documentation-generator skill
│   └── __init__.py
├── tests/                  # Test suite
├── docs/                   # Documentation
├── .env.example            # Environment template
├── docker-compose.yml      # Docker setup
└── pyproject.toml          # Dependencies
```


<br/>

## 🌟 Contributing

We love contributions! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/amazing-feature`
3. **Commit** your changes: `git commit -m 'Add amazing feature'`
4. **Push** to the branch: `git push origin feature/amazing-feature`
5. **Open** a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

**Built with [Bindu Agent Framework](https://github.com/getbindu/bindu)**

- 🌐 **A2A, AP2, X402 protocols** for Internet of Agents communication
- ⚡ **Zero-config setup** - from idea to production in minutes
- 🛠️ **Production-ready** out of the box

### Want to Build Your Own Agent?

```bash
# Create a new agent in 2 minutes
uvx cookiecutter https://github.com/getbindu/create-bindu-agent.git
```

---

<p align="center">
  <strong>Built with 💛 by the team from Amsterdam 🌷</strong>
</p>

<p align="center">
  <a href="https://github.com/lsvishaal/documentation-generator">⭐ Star this repo</a> •
  <a href="https://discord.gg/3w5zuYUuwt">💬 Join Discord</a> •
  <a href="https://docs.getbindu.com">📚 Bindu Docs</a>
</p>

<p align="center">
  <em>From idea to Internet of Agents in minutes. 🌻🚀✨</em>
</p>
