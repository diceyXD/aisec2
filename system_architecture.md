# Multi-Agent Security Testing Framework Architecture

This diagram illustrates the flow of data, tool execution, and inference requests within the system.

```mermaid
graph TD
    User([User / Security Intern]) -- Malicious/Test Prompts --> Orchestrator
    
    subgraph Docker Sandbox
        subgraph LangGraph Workflow
            State[(Shared Agent State)]
            Orchestrator[Orchestrator Agent]
            Researcher[Researcher Agent]
            Action[Action Agent]
            
            Orchestrator <--> State
            Researcher <--> State
            Action <--> State
            
            Orchestrator -- Routes Tasks --> Researcher
            Researcher -- Returns Results --> Orchestrator
            Orchestrator -- Routes Tasks --> Action
            Action -- Returns Results --> Orchestrator
        end
        
        Tool1[DuckDuckGo Search]
        Tool2[HTTP Fetch Probe]
        
        Researcher -. Calls .-> Tool1
        Action -. Calls .-> Tool2
    end
    
    subgraph Host Machine
        Ollama((Ollama Local LLM))
    end
    
    Orchestrator == Inference Request ==> Ollama
    Researcher == Inference Request ==> Ollama
    Action == Inference Request ==> Ollama
    
    Tool1 -. Web Request .-> Internet((Internet))
    Tool2 -. HTTP GET .-> TargetWeb((Target Websites))
```

### Key Components

1. **Docker Sandbox:** Encapsulates the entire multi-agent application to ensure that any malicious payloads injected during testing cannot escape and harm the host operating system.
2. **LangGraph Workflow:** Forces a "hub-and-spoke" design. All agents must route back to the Orchestrator, preventing infinite AI loops. All communication is recorded in the `Shared Agent State`.
3. **Local LLM (Ollama):** Running securely on the host machine. The Docker container communicates with it via `host.docker.internal`.
4. **Tool Isolation:** The Action Agent's network requests (`HTTP Fetch Probe`) are strictly limited to external websites, ensuring safe live-testing against targets.
