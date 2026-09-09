# AMBANK - Impact Analysis Demo Application

AMBANK is a comprehensive banking application designed to demonstrate code impact analysis capabilities across multiple programming languages and technologies.

## Architecture

AMBANK demonstrates a realistic banking system with the following components:

### Mainframe Components
- **DDM Files**: ADABAS Data Definition Modules
  - `ACCOUNT.ddm` - Account master (FILE 100)
  - `CUSTOMER.ddm` - Customer master (FILE 200)  
  - `TRANSACTION.ddm` - Transaction master (FILE 300)

- **Natural Programs**: Business logic layer
  - `ACCTRD001.nat` - Account read subprogram
  - `TXNWRT001.nat` - Transaction write subprogram
  - PDAs: `AMCA001.nat`, `AMTX001.nat`

- **COBOL Programs**: Processing layer
  - `ACCTUP001.cbl` - Account update program
  - `BRNPOS001.cbl` - Batch position program

- **JCL Jobs**: Mainframe job control
  - `ACCTUP001.jcl` - Account update job
  - `BRNPOS001.jcl` - Batch position job

### Modern Components
- **Python**: API layer
  - `account_api.py` - Account API client
  - `health_check.py` - Health check service

- **Shell Scripts**: Integration layer
  - `process_account.sh` - Account processing via CURL
  - `health_check.sh` - Health check via CURL

## Dependency Chain

The application demonstrates a complete dependency chain:

```
ACCOUNT.ddm (DDM) 
  → ACCTRD001.nat (Natural)
    → ACCTUP001.cbl (COBOL)
      → ACCTUP001.jcl (JCL)

TRANSACTION.ddm (DDM)
  → TXNWRT001.nat (Natural)
    → ACCTUP001.cbl (COBOL)
      → ACCTUP001.jcl (JCL)

account_api.py (Python)
  → process_account.sh (Shell)
    → HTTP Endpoint → ACCTUP001.jcl
```

## Impact Analysis Scenarios

### Scenario 1: DDM Schema Change
**Change**: Modify `ACCOUNT.ddm` field length
- Field `AI` (CURRENT-BALANCE): P15 → P18
**Impact**: 
- ACCTRD001.nat (uses ACCOUNT.ddm)
- ACCTUP001.cbl (calls ACCTRD001)
- ACCTUP001.jcl (executes ACCTUP001)

### Scenario 2: Natural Program Change
**Change**: Modify `ACCTRD001.nat` logic
- Add new validation for account status
**Impact**:
- ACCTUP001.cbl (calls ACCTRD001)
- TXNWRT001.nat (calls ACCTRD001)
- BRNPOS001.cbl (calls TXNWRT001)

### Scenario 3: COBOL Program Change
**Change**: Modify `ACCTUP001.cbl` validation
- Add new currency validation
**Impact**:
- ACCTUP001.jcl (executes ACCTUP001)

### Scenario 4: Python API Change
**Change**: Modify `account_api.py` parameters
- Add new `term_months` parameter
**Impact**:
- process_account.sh (called by account_api.py)
- HTTP endpoint dependency

### Scenario 5: Shell Script Change
**Change**: Modify `process_account.sh` CURL headers
- Add new authentication header
**Impact**:
- HTTP endpoint dependency

## Setup Instructions

### Prerequisites
- Natural/ADABAS parser configured
- COBOL parser configured
- JCL parser configured
- Python parser configured
- Shell parser configured

### Repository Structure
```
AMBANK/
├── mainframe/
│   ├── ddm/              # ADABAS DDM files
│   ├── natural/          # Natural programs
│   ├── cobol/            # COBOL programs
│   └── jcl/              # JCL jobs
├── python/               # Python API clients
├── shell/                # Shell integration scripts
├── config/               # Configuration files
└── .github/workflows/   # CI/CD workflows
```

## Impact Analysis Testing

### Creating PROD and QA Branches

```bash
# Create prod branch (baseline)
git checkout -b prod
git push origin prod

# Create qa branch (for changes)
git checkout prod
git checkout -b qa
git push origin qa
```

### Making Changes in QA

Modify any file in the QA branch to demonstrate impact analysis:

```bash
# Example: Change DDM field length
# Edit mainframe/ddm/ACCOUNT.ddm
# Change: FIELD=AI, 15, P, DE → FIELD=AI, 18, P, DE

git add .
git commit -m "Increase account balance field length"
git push origin qa
```

### Expected Impact Analysis Results

When comparing PROD vs QA, the impact analysis should detect:

1. **Modified Files**: The specific files changed
2. **Downstream Dependencies**: Programs that depend on changed files
3. **Producer-Consumer Compatibility**: Breaking changes between producers and consumers
4. **Semantic Changes**: Structural changes in code/schema
5. **HTTP Dependencies**: API endpoint changes

## License

Demo application for impact analysis demonstration purposes.
