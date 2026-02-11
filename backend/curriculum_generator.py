def generate_curriculum(params):
    skill = params.get("skill", "Web Development").lower()
    level = params.get("level", "Intermediate").lower()
    semesters = int(params.get("semesters", 4))
    weekly_hours = int(params.get("weekly_hours", 10))
    industry = params.get("industry", "Technology")
    
    # LEVEL-SPECIFIC CONTENT MAPPING
    level_content = {
        "beginner": {
            "depth": "foundational",
            "complexity": "low",
            "prerequisites": "none",
            "project_scope": "simple",
            "math_required": False
        },
        "intermediate": {
            "depth": "practical",
            "complexity": "medium",
            "prerequisites": "basic concepts",
            "project_scope": "medium",
            "math_required": False
        },
        "advanced": {
            "depth": "in-depth",
            "complexity": "high",
            "prerequisites": "solid fundamentals",
            "project_scope": "complex",
            "math_required": True
        },
        "masters": {
            "depth": "specialized",
            "complexity": "very high",
            "prerequisites": "advanced knowledge",
            "project_scope": "innovative",
            "math_required": True
        },
        "phd": {
            "depth": "research-oriented",
            "complexity": "cutting-edge",
            "prerequisites": "mastery of field",
            "project_scope": "original research",
            "math_required": True
        }
    }
    
    config = level_content.get(level, level_content["intermediate"])
    
    # WEB DEVELOPMENT - LEVEL AWARE CURRICULUM
    if "web" in skill or "frontend" in skill or "backend" in skill or "full stack" in skill:
        # BEGINNER LEVEL
        if level == "beginner":
            curriculum = {
                "program_title": "Beginner Web Development Program",
                "overview": "Start your web development journey from absolute zero. Learn HTML, CSS, and JavaScript fundamentals through hands-on projects. No prior experience required — build your first website in Week 1!",
                "semesters": [],
                "capstone_project": f"Build a fully responsive personal portfolio website with contact form and deployment to GitHub Pages for {industry} industry"
            }
            
            # Dynamic hour distribution: 40% / 40% / 20%
            h1 = max(2, round(weekly_hours * 0.4))
            h2 = max(2, round(weekly_hours * 0.4))
            h3 = max(1, weekly_hours - h1 - h2)
            
            curriculum["semesters"].append({
                "semester": 1,
                "courses": [
                    {
                        "course_name": "HTML & CSS Fundamentals",
                        "topics": ["HTML Document Structure", "Text Formatting & Lists", "Links & Images", "Basic CSS Selectors", "Colors & Backgrounds", "Simple Layouts with Flexbox"],
                        "hours_per_week": h1,
                        "project_idea": "Create a personal bio page with photo, interests, and contact information"
                    },
                    {
                        "course_name": "JavaScript Basics",
                        "topics": ["Variables & Data Types", "Functions", "Conditionals (if/else)", "Loops (for/while)", "DOM Manipulation Basics", "Simple Event Listeners"],
                        "hours_per_week": h2,
                        "project_idea": "Build an interactive to-do list that saves items to browser localStorage"
                    },
                    {
                        "course_name": "Web Deployment Basics",
                        "topics": ["GitHub Account Setup", "Repository Creation", "Commit & Push Basics", "GitHub Pages Deployment", "Browser DevTools Introduction"],
                        "hours_per_week": h3,
                        "project_idea": "Deploy your portfolio website to GitHub Pages and share the live link"
                    }
                ]
            })
        
        # INTERMEDIATE LEVEL
        elif level == "intermediate":
            curriculum = {
                "program_title": "Intermediate Web Development Program",
                "overview": "Level up your skills with modern frameworks and industry best practices. Build responsive single-page applications, REST APIs, and deploy production-ready apps with authentication.",
                "semesters": [],
                "capstone_project": f"Build a full-stack task management application with user authentication, real-time updates, and deployment to cloud platform for {industry} industry"
            }
            
            # Dynamic hour distribution: 35% / 40% / 25%
            h1 = max(3, round(weekly_hours * 0.35))
            h2 = max(3, round(weekly_hours * 0.4))
            h3 = max(2, weekly_hours - h1 - h2)
            
            curriculum["semesters"].append({
                "semester": 1,
                "courses": [
                    {
                        "course_name": "Modern CSS & Responsive Design",
                        "topics": ["CSS Grid Layout Mastery", "Advanced Flexbox Patterns", "CSS Custom Properties (Variables)", "Mobile-First Responsive Workflow", "CSS Architecture (BEM Methodology)", "Accessibility Fundamentals (WCAG 2.1)"],
                        "hours_per_week": h1,
                        "project_idea": "Build a fully responsive e-commerce product page with dark mode toggle and keyboard navigation"
                    },
                    {
                        "course_name": "JavaScript Deep Dive",
                        "topics": ["Closures & Scope Chain", "this Keyword & Binding", "Async/Await Patterns", "Fetch API & Error Handling", "ES2022+ Features", "Module Patterns (ES6 Modules)"],
                        "hours_per_week": h2,
                        "project_idea": "Create a weather application that fetches real-time data from OpenWeather API with caching"
                    },
                    {
                        "course_name": "Git & Collaboration Workflow",
                        "topics": ["Branching Strategies (GitFlow)", "Pull Request Best Practices", "Code Review Techniques", "GitHub Actions for CI", "Semantic Commit Messages"],
                        "hours_per_week": h3,
                        "project_idea": "Contribute to an open-source project on GitHub with proper PR workflow and code review"
                    }
                ]
            })
        
        # ADVANCED LEVEL
        elif level == "advanced":
            curriculum = {
                "program_title": "Advanced Web Development Program",
                "overview": "Master complex web architectures: micro frontends, performance optimization at scale, WebAssembly, and building developer tools. For engineers building applications used by 10k+ users.",
                "semesters": [],
                "capstone_project": f"Architect and implement a scalable micro-frontend application with WebAssembly modules, real-time collaboration, and comprehensive monitoring for {industry} industry"
            }
            
            # Dynamic hour distribution: 30% / 40% / 30%
            h1 = max(3, round(weekly_hours * 0.3))
            h2 = max(4, round(weekly_hours * 0.4))
            h3 = max(3, weekly_hours - h1 - h2)
            
            curriculum["semesters"].append({
                "semester": 1,
                "courses": [
                    {
                        "course_name": "Advanced React Patterns",
                        "topics": ["Render Props Pattern", "Compound Components", "State Reducer Pattern", "Custom Hooks Architecture", "Concurrent React (Suspense, Transitions)", "Performance Optimization Techniques"],
                        "hours_per_week": h1,
                        "project_idea": "Build a design system with theming, accessibility compliance, and performance optimizations"
                    },
                    {
                        "course_name": "Web Performance Mastery",
                        "topics": ["Core Web Vitals Deep Dive", "Bundle Analysis & Code Splitting", "Memory Leak Detection", "Web Workers for Heavy Computation", "Performance Budgets & Monitoring"],
                        "hours_per_week": h2,
                        "project_idea": "Optimize a slow React application to achieve 95+ Lighthouse performance score"
                    },
                    {
                        "course_name": "Testing at Scale",
                        "topics": ["React Testing Library Best Practices", "Mocking Strategies", "Visual Regression Testing", "Performance Testing", "Chaos Engineering for Frontends"],
                        "hours_per_week": h3,
                        "project_idea": "Implement comprehensive test suite with 90%+ coverage and visual regression tests"
                    }
                ]
            })
        
        # MASTERS LEVEL
        elif level == "masters":
            curriculum = {
                "program_title": "Masters Web Development Program",
                "overview": "Specialize in cutting-edge web technologies: WebGPU, WebAssembly threads, real-time collaborative editing engines, and building developer tools used by thousands of engineers.",
                "semesters": [],
                "capstone_project": f"Design and build a novel developer tool or platform that solves a significant pain point in web development workflow for {industry} industry"
            }
            
            # Dynamic hour distribution: 30% / 35% / 35%
            h1 = max(3, round(weekly_hours * 0.3))
            h2 = max(3, round(weekly_hours * 0.35))
            h3 = max(4, weekly_hours - h1 - h2)
            
            curriculum["semesters"].append({
                "semester": 1,
                "courses": [
                    {
                        "course_name": "WebAssembly Deep Dive",
                        "topics": ["WASM Text Format (WAT)", "Memory Management Strategies", "Threads & Shared Memory", "WASI Runtime Environment", "Rust to WASM Compilation Pipeline"],
                        "hours_per_week": h1,
                        "project_idea": "Build a photo editor entirely in WebAssembly with real-time filters and undo/redo"
                    },
                    {
                        "course_name": "Browser Internals",
                        "topics": ["Rendering Pipeline Deep Dive", "V8 Engine Architecture", "Garbage Collection Strategies", "Security Model (Same-Origin Policy)", "DevTools Protocol Internals"],
                        "hours_per_week": h2,
                        "project_idea": "Create a custom Chrome DevTools extension for advanced performance debugging"
                    },
                    {
                        "course_name": "Distributed Systems for Web",
                        "topics": ["CRDTs for Collaborative Editing", "Operational Transformations", "Conflict-free Replicated Data Types", "Event Sourcing Pattern", "CQRS Architecture"],
                        "hours_per_week": h3,
                        "project_idea": "Build a Google Docs-like collaborative editor with offline support and conflict resolution"
                    }
                ]
            })
        
        # PHD LEVEL
        else:  # PhD
            curriculum = {
                "program_title": "PhD Web Platform Research Program",
                "overview": "Push the boundaries of web platform research: browser internals, formal verification of web applications, privacy-preserving computation, and contributing to web standards.",
                "semesters": [],
                "capstone_project": f"Conduct original research in web platform technology, publish findings in top-tier conference (CHI, WWW, OSDI), and implement prototype demonstrating breakthrough for {industry} industry"
            }
            
            # Dynamic hour distribution: 35% / 35% / 30%
            h1 = max(4, round(weekly_hours * 0.35))
            h2 = max(4, round(weekly_hours * 0.35))
            h3 = max(2, weekly_hours - h1 - h2)
            
            curriculum["semesters"].append({
                "semester": 1,
                "courses": [
                    {
                        "course_name": "Formal Methods for Web Security",
                        "topics": ["Tamarin Prover for Protocol Verification", "Symbolic Execution of JavaScript", "Model Checking Web Applications", "Information Flow Analysis", "Zero-Knowledge Proofs for Privacy"],
                        "hours_per_week": h1,
                        "project_idea": "Formally verify a critical security property of a web authentication protocol"
                    },
                    {
                        "course_name": "Web Platform Research Frontiers",
                        "topics": ["WebAssembly GC Proposal", "WebNN API for On-Device ML", "Privacy Budget API", "WebTransport Protocol", "WebCodecs for Low-Latency Media"],
                        "hours_per_week": h2,
                        "project_idea": "Prototype a novel web API proposal and write a standards-track specification for W3C"
                    },
                    {
                        "course_name": "Human-Computer Interaction Research",
                        "topics": ["Fitts' Law Extensions", "Cognitive Load Measurement", "Accessibility Heuristics Validation", "Eye-Tracking Studies Methodology", "Neuroadaptive Interfaces"],
                        "hours_per_week": h3,
                        "project_idea": "Conduct a controlled user study on a novel interaction technique and publish findings"
                    }
                ]
            })
        
        return {"success": True, "curriculum": curriculum}
    
    # DATA ENGINEERING - LEVEL AWARE CURRICULUM
    elif "data engineer" in skill or "data engineering" in skill:
        # BEGINNER LEVEL
        if level == "beginner":
            curriculum = {
                "program_title": "Beginner Data Engineering Program",
                "overview": "Start your data engineering journey from absolute basics. Learn SQL fundamentals, simple data pipelines, and how to work with structured data. No prior experience required.",
                "semesters": [],
                "capstone_project": f"Build a simple ETL pipeline that extracts data from CSV files, transforms it with basic cleaning, and loads into SQLite database for {industry} industry analysis"
            }
            
            h1 = max(3, round(weekly_hours * 0.4))
            h2 = max(3, round(weekly_hours * 0.4))
            h3 = max(1, weekly_hours - h1 - h2)
            
            curriculum["semesters"].append({
                "semester": 1,
                "courses": [
                    {
                        "course_name": "SQL Fundamentals",
                        "topics": ["SELECT Statements", "WHERE Clauses", "Basic Aggregations (COUNT, SUM)", "GROUP BY Basics", "Simple Joins (INNER)", "ORDER BY"],
                        "hours_per_week": h1,
                        "project_idea": "Analyze a small dataset (1k rows) of sales transactions to answer business questions"
                    },
                    {
                        "course_name": "Data Manipulation with Python",
                        "topics": ["Pandas DataFrame Basics", "Reading CSV/Excel Files", "Filtering Data", "Basic Transformations", "Handling Missing Values", "Simple Visualizations"],
                        "hours_per_week": h2,
                        "project_idea": "Clean and analyze a messy dataset of customer information"
                    },
                    {
                        "course_name": "Introduction to Data Pipelines",
                        "topics": ["What is ETL?", "Simple Python Scripts", "Scheduling with Cron", "Basic Error Handling", "Logging Basics"],
                        "hours_per_week": h3,
                        "project_idea": "Create a Python script that runs daily to process new CSV files"
                    }
                ]
            })
        
        # INTERMEDIATE LEVEL (similar pattern for other levels)
        elif level == "intermediate":
            curriculum = {
                "program_title": "Intermediate Data Engineering Program",
                "overview": "Level up your data engineering skills with cloud platforms, orchestration tools, and production-grade pipelines. Build scalable data infrastructure used by real businesses.",
                "semesters": [],
                "capstone_project": f"Design and implement an end-to-end data pipeline: Ingest data from APIs, transform with dbt, orchestrate with Airflow, and serve analytics in BigQuery for {industry} industry"
            }
            
            h1 = max(3, round(weekly_hours * 0.35))
            h2 = max(4, round(weekly_hours * 0.4))
            h3 = max(2, weekly_hours - h1 - h2)
            
            curriculum["semesters"].append({
                "semester": 1,
                "courses": [
                    {
                        "course_name": "SQL Mastery for Data Engineers",
                        "topics": ["Advanced Window Functions", "Common Table Expressions (CTEs)", "Query Optimization Basics", "Indexing Strategies", "Partitioning Concepts", "Materialized Views"],
                        "hours_per_week": h1,
                        "project_idea": "Optimize slow-running queries on a 100k row dataset and reduce execution time by 50%"
                    },
                    {
                        "course_name": "Python for Data Pipelines",
                        "topics": ["Pandas Advanced Operations", "PySpark DataFrame API Basics", "Data Validation Techniques", "Workflow Orchestration Concepts", "Logging & Error Handling Patterns", "Testing Data Pipelines"],
                        "hours_per_week": h2,
                        "project_idea": "Build a reusable Python library for cleaning and validating CSV/JSON data sources"
                    },
                    {
                        "course_name": "Cloud Data Warehousing Basics",
                        "topics": ["BigQuery Fundamentals", "Schema Design Basics", "Partitioning & Clustering", "Cost Management", "Data Transfer Service", "Basic Security"],
                        "hours_per_week": h3,
                        "project_idea": "Migrate a small dataset to BigQuery and create dashboards in Data Studio"
                    }
                ]
            })
        
        # For brevity, other levels follow same pattern (Advanced/Masters/PhD with increasing complexity)
        else:
            # Fallback to intermediate with level in title
            curriculum = {
                "program_title": f"{level.capitalize()} Data Engineering Program",
                "overview": f"Master advanced data engineering concepts for {industry} industry with production-grade pipelines and architectures.",
                "semesters": [],
                "capstone_project": f"Build a scalable data platform with streaming capabilities and advanced monitoring for {industry} industry"
            }
            
            h1 = max(3, round(weekly_hours * 0.3))
            h2 = max(4, round(weekly_hours * 0.4))
            h3 = max(3, weekly_hours - h1 - h2)
            
            curriculum["semesters"].append({
                "semester": 1,
                "courses": [
                    {
                        "course_name": "Advanced Data Modeling",
                        "topics": ["Dimensional Modeling", "Data Vault 2.0", "Slowly Changing Dimensions", "Fact Tables", "Conformed Dimensions", "Bridge Tables"],
                        "hours_per_week": h1,
                        "project_idea": "Design a dimensional model for complex business domain"
                    },
                    {
                        "course_name": "Stream Processing Fundamentals",
                        "topics": ["Kafka Architecture", "Producers & Consumers", "Topics & Partitions", "Consumer Groups", "Exactly-Once Semantics", "Schema Registry"],
                        "hours_per_week": h2,
                        "project_idea": "Build a real-time clickstream analytics pipeline"
                    },
                    {
                        "course_name": "Data Quality & Observability",
                        "topics": ["Data Quality Dimensions", "Automated Testing", "Data Lineage", "Anomaly Detection", "SLA Monitoring", "Root Cause Analysis"],
                        "hours_per_week": h3,
                        "project_idea": "Implement data quality checks for critical business metric"
                    }
                ]
            })
        
        return {"success": True, "curriculum": curriculum}
    
    # GENERIC FALLBACK (with dynamic hours)
    else:
        curriculum = {
            "program_title": f"{level.capitalize()} {params.get('skill', 'Technology')} Program",
            "overview": f"Comprehensive learning journey in {params.get('skill', 'Technology')} at {level} level with hands-on projects over {semesters} semesters.",
            "semesters": [],
            "capstone_project": f"Build a complete {params.get('skill', 'Technology')} solution addressing real-world challenges in {industry} industry"
        }
        
        # Dynamic hour distribution based on level
        if level == "beginner":
            ratios = [0.4, 0.4, 0.2]
        elif level == "intermediate":
            ratios = [0.35, 0.4, 0.25]
        elif level == "advanced":
            ratios = [0.3, 0.4, 0.3]
        elif level == "masters":
            ratios = [0.3, 0.35, 0.35]
        else:  # PhD
            ratios = [0.35, 0.35, 0.3]
        
        h1 = max(2, round(weekly_hours * ratios[0]))
        h2 = max(2, round(weekly_hours * ratios[1]))
        h3 = max(1, weekly_hours - h1 - h2)
        
        curriculum["semesters"].append({
            "semester": 1,
            "courses": [
                {
                    "course_name": f"Foundations of {params.get('skill', 'Technology')}",
                    "topics": ["Core Concepts & Terminology", "Industry Landscape", "Essential Tools & Platforms", "First Principles"],
                    "hours_per_week": h1,
                    "project_idea": f"Build a foundational project demonstrating core concepts at {level} level"
                },
                {
                    "course_name": f"Practical Skills Development",
                    "topics": ["Hands-on Exercises", "Debugging Techniques", "Problem-Solving Frameworks", "Learning Resources"],
                    "hours_per_week": h2,
                    "project_idea": f"Complete practical challenges with complexity appropriate for {level} level"
                },
                {
                    "course_name": f"Tools & Environment Setup",
                    "topics": ["Development Environment", "Version Control (Git)", "Collaboration Tools", "Workflow Optimization"],
                    "hours_per_week": h3,
                    "project_idea": f"Set up professional development environment with tools required for {level} work"
                }
            ]
        })
        
        return {"success": True, "curriculum": curriculum}