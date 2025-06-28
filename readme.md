# UKA IZKF Genomics Facility BPM Repository

This repository contains bioinformatics templates and workflows for the [BPM (Bioinformatics Project Manager)](https://github.com/chaochungkuo/BPM) tool, specifically configured for the Genomics Facility at the Interdisciplinary Center for Clinical Research (IZKF), University Hospital RWTH Aachen.

## What is BPM?

BPM is a flexible, template-driven CLI tool for managing bioinformatics projects. It helps standardize project structures, automate workflows, and ensure reproducibility across research projects.

📖 **Documentation**: [https://chaochungkuo.github.io/BPM/](https://chaochungkuo.github.io/BPM/)

## Quick Start

### 1. Install BPM
```bash
pip install bpm
export BPM_CACHE="/path/to/your/bpm_cache"
```

### 2. Add this repository to BPM
```bash
# Add to BPM
bpm repo add https://github.com/chaochungkuo/BPM_repo.git
```

### 3. Use the templates and workflows
```bash
# List available templates
bpm generate --list

# List available workflows
bpm run --list

# Create a new project
bpm init 240101_RNAseq_Study_UKA_Research

# Generate files from a template
bpm generate demultiplexing:bclconvert --project project.yaml

# Run a workflow
bpm run workflows:generate_nfcore_rnaseq_samplesheet --project project.yaml
```

## Repository Structure Overview

This BPM repository is organized into five main folder types, each serving a specific purpose in the bioinformatics workflow:

| Folder | Purpose |
|--------|---------|
| [**`config/`**](https://github.com/IZKF-Genomics/BPM_repo/tree/main/config) | Facility/environment settings |
| [**`templates/`**](https://github.com/IZKF-Genomics/BPM_repo/tree/main/templates) | Ready-to-use scripts and files |
| [**`resolvers/`**](https://github.com/IZKF-Genomics/BPM_repo/tree/main/resolvers) | Dynamic parameter resolution |
| [**`post_hooks/`**](https://github.com/IZKF-Genomics/BPM_repo/tree/main/post_hooks) | Post-rendering customization |
| [**`workflows/`**](https://github.com/IZKF-Genomics/BPM_repo/tree/main/workflows) | Cross-project utility scripts |

## Detailed Folder Explanations

### `config/`
**Purpose**: Contains all facility or environment specific settings and configuration that is independent from any project or templates.

**Key Features**:
- Global settings that persist across all projects
- Environment-specific configurations
- Team/institution level settings
- Rarely changed once configured

**Files**:
- `environment.yaml` - Environment-specific settings and variables
- `main.yaml` - Main repository configuration and metadata

### `templates/`
**Purpose**: Sets of scripts and files for particular purposes that can be rendered according to command parameters, project information, or template configuration.

**Key Features**:
- Project-specific file generation
- User chooses which templates to apply
- Configurable via parameters
- Each template has its own `template_config.yaml`

### `resolvers/`
**Purpose**: Simple functions to resolve input or output parameters for templates. Any template or variable specific function should go here instead of into the core function of BPM.

**Key Features**:
- Template-specific parameter resolution
- Dynamic value computation
- Automatic execution during rendering
- Keeps BPM core clean and modular

### `post_hooks/`
**Purpose**: Functions executed after a template is rendered. They are not bound by any parameters and give users freedom to customize the template in the way they want.

**Key Features**:
- High customization freedom
- User-defined logic execution
- Post-processing and cleanup
- Project-specific customization

### `workflows/`
**Purpose**: Scripts applied inside a project across all templates and results, or executed outside a project as a handy command. Any useful scripts not relevant to a specific template can go here.

**Key Features**:
- Can be project-specific or standalone
- Cross-template functionality
- User explicitly chooses to run
- Complete control over execution

## Customizing for Your Team

This repository serves as a template for creating your own BPM repository:

### 1. Fork this repository
```bash
# Fork on GitHub, then clone your fork
git clone https://github.com/your-username/your-bpm-repo.git
```

### 2. Customize the configuration
Edit `repo.yaml` to update:
- Repository name and description
- Maintainer information
- Default templates and workflows

### 3. Add your own templates
- Place templates in the `templates/` directory
- Update `repo.yaml` with template metadata
- Add any required dependencies

### 4. Add your own workflows
- Place workflow scripts in the `workflows/` directory
- Update `repo.yaml` with workflow configurations
- Test with your BPM installation

### 5. Share with your team
- Push your customized repository to your organization's Git server
- Team members can add it with: `bpm repo add /path/to/your/repo`

## Support

- **BPM Documentation**: [https://chaochungkuo.github.io/BPM/](https://chaochungkuo.github.io/BPM/)
- **BPM Issues**: [https://github.com/chaochungkuo/BPM/issues](https://github.com/chaochungkuo/BPM/issues)
- **This Repository**: Contact the Genomics Facility team

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
