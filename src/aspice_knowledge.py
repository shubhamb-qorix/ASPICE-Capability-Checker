# ASPICE v4.0 Capability Levels and Process Attribute definitions
CAPABILITY_LEVELS = {
    0: {
        "name": "Incomplete",
        "description": "The process is not implemented or fails to achieve its process purpose. "
                       "Little or no evidence of any systematic achievement of the process purpose.",
        "process_attributes": [],
        "rating_scale": "N (Not achieved): 0-15%",
    },
    1: {
        "name": "Performed",
        "description": "The implemented process achieves its process purpose.",
        "process_attributes": [
            {
                "id": "PA 1.1",
                "name": "Process Performance",
                "description": "The extent to which the process achieves its defined process outcomes.",
                "indicators": [
                    "Process outcomes are achieved",
                    "Base practices are performed",
                    "Work products are produced",
                ],
            }
        ],
        "rating_scale": "Fully achieved (F): 85-100%, Largely achieved (L): 50-85%, "
                        "Partially achieved (P): 15-50%, Not achieved (N): 0-15%",
    },
    2: {
        "name": "Managed",
        "description": "The previously described Performed process is now implemented in a managed "
                       "fashion (planned, monitored and adjusted) and its work products are appropriately "
                       "established, controlled and maintained.",
        "process_attributes": [
            {
                "id": "PA 2.1",
                "name": "Performance Management",
                "description": "The extent to which the performance of the process is managed.",
                "indicators": [
                    "Objectives for the performance of the process are identified",
                    "Performance of the process is planned",
                    "Performance of the process is monitored",
                    "Performance of the process is adjusted to meet plans",
                    "Responsibilities and authorities for performing the process are defined",
                    "Personnel performing the process are prepared",
                    "Resources and information necessary for performing the process are identified",
                    "Interfaces between the involved parties are managed",
                ],
            },
            {
                "id": "PA 2.2",
                "name": "Work Product Management",
                "description": "The extent to which the work products produced by the process are appropriately managed.",
                "indicators": [
                    "Requirements for the work products of the process are defined",
                    "Requirements for documentation and control of the work products are defined",
                    "Work products are appropriately identified, documented and controlled",
                    "Work products are reviewed in accordance with planned arrangements",
                ],
            },
        ],
        "rating_scale": "Fully achieved (F): 85-100%, Largely achieved (L): 50-85%, "
                        "Partially achieved (P): 15-50%, Not achieved (N): 0-15%",
    },
    3: {
        "name": "Established",
        "description": "The previously described Managed process is now implemented using a defined "
                       "process that is capable of achieving its process outcomes.",
        "process_attributes": [
            {
                "id": "PA 3.1",
                "name": "Process Definition",
                "description": "The extent to which a standard process is maintained to support the "
                               "deployment of the defined process.",
                "indicators": [
                    "A standard process, including appropriate tailoring guidelines, is defined",
                    "The sequence and interaction of the standard process with other processes is determined",
                    "Required competencies and roles for performing the standard process are identified",
                    "Required infrastructure and work environment for performing the standard process are identified",
                    "Suitable methods to monitor the effectiveness and suitability of the standard process are determined",
                ],
            },
            {
                "id": "PA 3.2",
                "name": "Process Deployment",
                "description": "The extent to which the standard process is effectively deployed as a "
                               "defined process to achieve its process outcomes.",
                "indicators": [
                    "A defined process is deployed based upon an appropriately selected and/or tailored standard process",
                    "Required roles, responsibilities and authorities for performing the defined process are assigned",
                    "Personnel performing the defined process are competent",
                    "Required resources and information necessary for performing the defined process are available",
                    "Required infrastructure and work environment for performing the defined process are available",
                    "Appropriate data are collected and analysed to demonstrate the suitability and effectiveness of the process",
                ],
            },
        ],
        "rating_scale": "Fully achieved (F): 85-100%, Largely achieved (L): 50-85%, "
                        "Partially achieved (P): 15-50%, Not achieved (N): 0-15%",
    },
    4: {
        "name": "Predictable",
        "description": "The previously described Established process now operates within defined limits "
                       "to achieve its process outcomes.",
        "process_attributes": [
            {
                "id": "PA 4.1",
                "name": "Quantitative Analysis",
                "description": "The extent to which the process is quantitatively analysed to determine "
                               "if the process performance is contributing to achievement of relevant "
                               "quality and process performance objectives.",
                "indicators": [
                    "Process information needs in support of relevant defined quality and process performance objectives are identified",
                    "Process measurement objectives are derived from process information needs",
                    "Quantitative objectives for process performance in support of quality and process performance objectives are established",
                    "Measures and frequency of measurement are identified",
                    "Measurement results are collected, analysed and reported",
                    "Quantitative measurement results are used to characterise process performance",
                ],
            },
            {
                "id": "PA 4.2",
                "name": "Quantitative Control",
                "description": "The extent to which the process is quantitatively managed to produce "
                               "a process that is stable, capable and predictable within defined limits.",
                "indicators": [
                    "Analysis techniques are used to identify special causes of variation in process performance",
                    "Corrective actions are taken to address root causes of special cause variation",
                    "Control limits are established for normal process performance",
                    "Measurement data are analysed for special causes of process variation",
                    "Corrective actions are taken when control limits are exceeded",
                ],
            },
        ],
        "rating_scale": "Fully achieved (F): 85-100%, Largely achieved (L): 50-85%, "
                        "Partially achieved (P): 15-50%, Not achieved (N): 0-15%",
    },
    5: {
        "name": "Optimizing",
        "description": "The previously described Predictable process is continuously improved to meet "
                       "relevant current and projected business goals.",
        "process_attributes": [
            {
                "id": "PA 5.1",
                "name": "Process Innovation",
                "description": "The extent to which changes to the process are identified from analysis "
                               "of common causes of variation in performance, and from investigations of "
                               "innovative approaches to the definition and deployment of the process.",
                "indicators": [
                    "Process improvement objectives for the process are defined that support the relevant business goals",
                    "Appropriate data are analysed to identify common causes of variations in process performance",
                    "Appropriate data are analysed to identify opportunities for best practice and innovation",
                    "Improvement opportunities derived from new technologies and process concepts are identified",
                    "An implementation strategy is derived to achieve process improvement objectives",
                ],
            },
            {
                "id": "PA 5.2",
                "name": "Process Optimization",
                "description": "The extent to which changes to the definition, management and performance "
                               "of the process result in effective impact that achieves the relevant "
                               "process improvement objectives.",
                "indicators": [
                    "Impact of all proposed changes is assessed against the objectives of the defined process and standard process",
                    "Implementation of all agreed changes is managed to ensure that any disruption to process performance is understood and controlled",
                    "Effectiveness of process change on the basis of actual performance is evaluated against the defined product requirements and process objectives",
                ],
            },
        ],
        "rating_scale": "Fully achieved (F): 85-100%, Largely achieved (L): 50-85%, "
                        "Partially achieved (P): 15-50%, Not achieved (N): 0-15%",
    },
}

# ASPICE v4.0 Process Reference Model (PRM) - Process Groups
PROCESS_GROUPS = {
    "SWE": {
        "name": "Software Engineering",
        "processes": {
            "SWE.1": {
                "name": "Software Requirements Analysis",
                "purpose": "The purpose of the Software Requirements Analysis Process is to transform the "
                           "defined software requirements into a set of software requirements that can be "
                           "used to guide the software design.",
                "outcomes": [
                    "SWE.1.O1: Defined and refined software requirements are established",
                    "SWE.1.O2: Software requirements are analysed for correctness and testability",
                    "SWE.1.O3: The impact of software requirements on the operating environment is understood",
                    "SWE.1.O4: Prioritisation for implementing software requirements is defined",
                    "SWE.1.O5: Software requirements are updated as needed",
                    "SWE.1.O6: Changes to software requirements are managed",
                    "SWE.1.O7: Software requirements are communicated to all affected parties",
                ],
                "work_products": [
                    "13-04: Software Requirements Specification",
                    "13-19: Traceability Record",
                ],
                "base_practices": [
                    "SWE.1.BP1: Specify software requirements",
                    "SWE.1.BP2: Structure software requirements",
                    "SWE.1.BP3: Analyse software requirements",
                    "SWE.1.BP4: Analyse the impact on the operating environment",
                    "SWE.1.BP5: Define acceptance criteria for software requirements",
                    "SWE.1.BP6: Ensure consistency and bilateral traceability",
                    "SWE.1.BP7: Identify the content of software release note",
                ],
            },
            "SWE.2": {
                "name": "Software Architectural Design",
                "purpose": "The purpose of the Software Architectural Design Process is to establish an "
                           "architectural design for the software that allows for the implementation of "
                           "the software requirements.",
                "outcomes": [
                    "SWE.2.O1: A software architectural design is defined",
                    "SWE.2.O2: The software requirements are allocated to the elements of the software architecture",
                    "SWE.2.O3: Interfaces of software elements are defined",
                    "SWE.2.O4: Consistency and traceability between software requirements and software architectural design are established",
                    "SWE.2.O5: Communication mechanisms across internal and external interfaces are evaluated and defined",
                ],
                "work_products": [
                    "04-04: Software Architectural Design Document",
                    "13-19: Traceability Record",
                ],
                "base_practices": [
                    "SWE.2.BP1: Develop software architectural design",
                    "SWE.2.BP2: Allocate software requirements to the software elements",
                    "SWE.2.BP3: Define interfaces of software elements",
                    "SWE.2.BP4: Describe dynamic behaviour",
                    "SWE.2.BP5: Evaluate alternative architectures",
                    "SWE.2.BP6: Establish bidirectional traceability",
                ],
            },
            "SWE.3": {
                "name": "Software Detailed Design and Unit Construction",
                "purpose": "The purpose of the Software Detailed Design and Unit Construction Process is "
                           "to provide an evaluated detailed design for the software and to produce and "
                           "evaluate the software units.",
                "outcomes": [
                    "SWE.3.O1: A detailed design of the software is developed",
                    "SWE.3.O2: Interfaces of software units are defined",
                    "SWE.3.O3: Software units are produced",
                    "SWE.3.O4: Consistency and traceability between software architectural design and software detailed design are established",
                    "SWE.3.O5: Consistency and traceability are established between software detailed design and software units",
                ],
                "work_products": [
                    "04-06: Software Detailed Design",
                    "16-07: Software Unit",
                    "13-19: Traceability Record",
                ],
                "base_practices": [
                    "SWE.3.BP1: Develop software detailed design",
                    "SWE.3.BP2: Define interfaces of software units",
                    "SWE.3.BP3: Describe dynamic behaviour",
                    "SWE.3.BP4: Evaluate software detailed design",
                    "SWE.3.BP5: Construct software units",
                    "SWE.3.BP6: Evaluate software units",
                    "SWE.3.BP7: Establish bidirectional traceability",
                ],
            },
            "SWE.4": {
                "name": "Software Unit Verification",
                "purpose": "The purpose of the Software Unit Verification Process is to verify software "
                           "units to provide evidence for compliance of the software units with the "
                           "software detailed design and with non-functional requirements.",
                "outcomes": [
                    "SWE.4.O1: A unit verification strategy including regression strategy is developed to verify the software units",
                    "SWE.4.O2: Criteria for unit verification are defined",
                    "SWE.4.O3: Unit verification of software units is performed",
                    "SWE.4.O4: Results of unit verification are made available",
                    "SWE.4.O5: Consistency and bidirectional traceability are established between software unit test cases/procedures and software detailed design",
                ],
                "work_products": [
                    "08-16: Unit Verification Plan",
                    "08-52: Unit Verification Specification",
                    "13-19: Traceability Record",
                    "13-50: Verification Results",
                ],
                "base_practices": [
                    "SWE.4.BP1: Develop unit verification strategy and regression strategy",
                    "SWE.4.BP2: Develop criteria for unit verification",
                    "SWE.4.BP3: Perform unit verification",
                    "SWE.4.BP4: Establish bidirectional traceability",
                    "SWE.4.BP5: Ensure consistency",
                ],
            },
            "SWE.5": {
                "name": "Software Integration and Integration Test",
                "purpose": "The purpose of the Software Integration and Integration Test Process is to "
                           "integrate the software units into larger software items up to a complete "
                           "software and to ensure that the integrated software items are tested to "
                           "provide evidence for compliance of the integrated software items with the "
                           "software architectural design.",
                "outcomes": [
                    "SWE.5.O1: An integration strategy is defined for integrating the software units and software items",
                    "SWE.5.O2: A test strategy including regression strategy for integration testing is developed",
                    "SWE.5.O3: Software units and software items are integrated up to a complete software item",
                    "SWE.5.O4: Integrated software items are verified",
                    "SWE.5.O5: Results of integration verification are evaluated for consistency with requirements",
                    "SWE.5.O6: Bidirectional traceability is established between test cases and software requirements",
                ],
                "work_products": [
                    "08-50: Software Integration Test Plan",
                    "08-52: Software Integration Test Specification",
                    "13-19: Traceability Record",
                    "13-50: Verification Results",
                ],
                "base_practices": [
                    "SWE.5.BP1: Develop software integration strategy",
                    "SWE.5.BP2: Develop software integration test strategy including regression strategy",
                    "SWE.5.BP3: Integrate software units and software items",
                    "SWE.5.BP4: Define integration test cases",
                    "SWE.5.BP5: Perform software integration testing",
                    "SWE.5.BP6: Establish bidirectional traceability",
                    "SWE.5.BP7: Ensure consistency",
                ],
            },
            "SWE.6": {
                "name": "Software Qualification Test",
                "purpose": "The purpose of the Software Qualification Test Process is to ensure that the "
                           "integrated software is tested to provide evidence for compliance of the software "
                           "with the software requirements.",
                "outcomes": [
                    "SWE.6.O1: A qualification test strategy including regression strategy is developed to ensure compliance with software requirements",
                    "SWE.6.O2: Criteria for software qualification are defined",
                    "SWE.6.O3: Software is tested to provide evidence for compliance with software requirements",
                    "SWE.6.O4: Results of software qualification testing are evaluated",
                    "SWE.6.O5: Bidirectional traceability is established between software test cases and software requirements",
                ],
                "work_products": [
                    "08-50: Software Qualification Test Plan",
                    "08-52: Software Qualification Test Specification",
                    "13-19: Traceability Record",
                    "13-50: Verification Results",
                ],
                "base_practices": [
                    "SWE.6.BP1: Develop software qualification test strategy including regression strategy",
                    "SWE.6.BP2: Develop criteria for software qualification",
                    "SWE.6.BP3: Test software",
                    "SWE.6.BP4: Establish bidirectional traceability",
                    "SWE.6.BP5: Ensure consistency",
                ],
            },
        },
    },
    "SYS": {
        "name": "System Engineering",
        "processes": {
            "SYS.1": {
                "name": "Requirements Elicitation",
                "purpose": "The purpose of the Requirements Elicitation Process is to gather, process and "
                           "track evolving stakeholder needs and requirements throughout the lifecycle of "
                           "the product and/or service so as to establish a requirements baseline that "
                           "serves as the basis for defining the needed work products.",
                "outcomes": [
                    "SYS.1.O1: Stakeholder requirements are defined",
                    "SYS.1.O2: Stakeholder requirements are analysed",
                    "SYS.1.O3: Stakeholder requirements are prioritised",
                    "SYS.1.O4: Changes to stakeholder requirements are managed",
                ],
                "work_products": [
                    "13-05: Stakeholder Requirements Specification",
                    "13-19: Traceability Record",
                ],
                "base_practices": [
                    "SYS.1.BP1: Obtain stakeholder requirements",
                    "SYS.1.BP2: Understand stakeholder expectations",
                    "SYS.1.BP3: Agree on stakeholder requirements",
                    "SYS.1.BP4: Establish stakeholder requirements baseline",
                ],
            },
            "SYS.2": {
                "name": "System Requirements Analysis",
                "purpose": "The purpose of the System Requirements Analysis Process is to transform the "
                           "defined stakeholder requirements into a set of system requirements that will "
                           "guide the design of the system.",
                "outcomes": [
                    "SYS.2.O1: System requirements are defined and maintained",
                    "SYS.2.O2: System requirements are structured and prioritised",
                    "SYS.2.O3: System requirements are analysed for correctness and verifiability",
                    "SYS.2.O4: System requirements are updated as needed",
                    "SYS.2.O5: Consistency and bidirectional traceability are established between system requirements and stakeholder requirements",
                ],
                "work_products": [
                    "13-04: System Requirements Specification",
                    "13-19: Traceability Record",
                ],
                "base_practices": [
                    "SYS.2.BP1: Specify system requirements",
                    "SYS.2.BP2: Structure system requirements",
                    "SYS.2.BP3: Analyse system requirements",
                    "SYS.2.BP4: Analyse impact on operational design",
                    "SYS.2.BP5: Define acceptance criteria for system requirements",
                    "SYS.2.BP6: Establish bidirectional traceability",
                ],
            },
            "SYS.3": {
                "name": "System Architectural Design",
                "purpose": "The purpose of the System Architectural Design Process is to establish a "
                           "system architectural design and identify which system requirements are to be "
                           "allocated to which elements of the system.",
                "outcomes": [
                    "SYS.3.O1: A system architectural design is developed and maintained",
                    "SYS.3.O2: The system requirements are allocated to the elements of the system architecture",
                    "SYS.3.O3: Interfaces between system elements and with external systems are defined",
                    "SYS.3.O4: Consistency and bidirectional traceability are established between system requirements and system architectural design",
                    "SYS.3.O5: Dynamic behaviour of the system elements is defined",
                ],
                "work_products": [
                    "04-04: System Architectural Design Document",
                    "13-19: Traceability Record",
                ],
                "base_practices": [
                    "SYS.3.BP1: Develop system architectural design",
                    "SYS.3.BP2: Allocate system requirements to system elements",
                    "SYS.3.BP3: Define interfaces of system elements",
                    "SYS.3.BP4: Describe dynamic behaviour",
                    "SYS.3.BP5: Evaluate alternative architectures",
                    "SYS.3.BP6: Establish bidirectional traceability",
                ],
            },
            "SYS.4": {
                "name": "System Integration and Integration Test",
                "purpose": "The purpose of the System Integration and Integration Test Process is to "
                           "integrate the system elements and to ensure that the integrated system items "
                           "are tested to provide evidence for compliance of the integrated system items "
                           "with the system architectural design.",
                "outcomes": [
                    "SYS.4.O1: A system integration strategy is defined",
                    "SYS.4.O2: A system integration test strategy is developed",
                    "SYS.4.O3: System elements are integrated",
                    "SYS.4.O4: Integrated system items are verified",
                    "SYS.4.O5: Results of the system integration test are evaluated",
                ],
                "work_products": [
                    "08-50: System Integration Test Plan",
                    "08-52: System Integration Test Specification",
                    "13-19: Traceability Record",
                    "13-50: Verification Results",
                ],
                "base_practices": [
                    "SYS.4.BP1: Develop system integration strategy",
                    "SYS.4.BP2: Develop integration test strategy",
                    "SYS.4.BP3: Integrate system elements",
                    "SYS.4.BP4: Perform system integration testing",
                    "SYS.4.BP5: Establish bidirectional traceability",
                ],
            },
            "SYS.5": {
                "name": "System Qualification Test",
                "purpose": "The purpose of the System Qualification Test Process is to ensure that the "
                           "integrated system is tested to provide evidence for compliance of the system "
                           "with the system requirements and that the system is ready for delivery.",
                "outcomes": [
                    "SYS.5.O1: A system qualification test strategy is developed",
                    "SYS.5.O2: Criteria for system qualification are defined",
                    "SYS.5.O3: System is tested to demonstrate compliance with system requirements",
                    "SYS.5.O4: Results of system qualification tests are evaluated",
                    "SYS.5.O5: Consistency and bidirectional traceability are established between system qualification test cases and system requirements",
                ],
                "work_products": [
                    "08-50: System Qualification Test Plan",
                    "08-52: System Qualification Test Specification",
                    "13-19: Traceability Record",
                    "13-50: Verification Results",
                ],
                "base_practices": [
                    "SYS.5.BP1: Develop system qualification test strategy",
                    "SYS.5.BP2: Develop criteria for system qualification",
                    "SYS.5.BP3: Test system",
                    "SYS.5.BP4: Establish bidirectional traceability",
                    "SYS.5.BP5: Ensure consistency",
                ],
            },
        },
    },
    "MAN": {
        "name": "Management",
        "processes": {
            "MAN.3": {
                "name": "Project Management",
                "purpose": "The purpose of the Project Management Process is to identify, establish, "
                           "coordinate and monitor the activities, tasks and resources necessary for a "
                           "project to produce a product and/or service in the context of the project "
                           "requirements and constraints.",
                "outcomes": [
                    "MAN.3.O1: The scope of the work for the project is defined",
                    "MAN.3.O2: Feasibility of achieving the goals of the project with available resources and constraints is evaluated",
                    "MAN.3.O3: The activities and resources necessary to complete the work are sized and estimated",
                    "MAN.3.O4: Interfaces within the project and with other projects and organisational units are identified",
                    "MAN.3.O5: Plans for the execution of the project are developed, implemented and maintained",
                    "MAN.3.O6: Progress of the project is monitored against the plans and information is used to correct deviations from plan",
                    "MAN.3.O7: Completion of the project with achieved results is verified against agreed goals",
                ],
                "work_products": [
                    "08-12: Project Plan",
                    "08-16: Project Status Report",
                    "13-04: Project Management Plan",
                ],
                "base_practices": [
                    "MAN.3.BP1: Define scope of work",
                    "MAN.3.BP2: Define project lifecycle",
                    "MAN.3.BP3: Evaluate feasibility",
                    "MAN.3.BP4: Define and monitor project activities",
                    "MAN.3.BP5: Ensure required skills, knowledge and experience",
                    "MAN.3.BP6: Monitor and control project",
                    "MAN.3.BP7: Manage project risks",
                    "MAN.3.BP8: Close project",
                ],
            },
            "MAN.5": {
                "name": "Risk Management",
                "purpose": "The purpose of the Risk Management Process is to continuously identify, "
                           "analyse, treat and monitor the risks.",
                "outcomes": [
                    "MAN.5.O1: A risk management strategy is defined",
                    "MAN.5.O2: Risks in the project are identified",
                    "MAN.5.O3: Risks are analysed and prioritised",
                    "MAN.5.O4: Risk treatment actions are defined, applied and evaluated",
                    "MAN.5.O5: Risks are monitored and communicated",
                ],
                "work_products": [
                    "08-16: Risk Management Plan",
                    "08-52: Risk Register",
                ],
                "base_practices": [
                    "MAN.5.BP1: Establish risk management scope",
                    "MAN.5.BP2: Identify risks",
                    "MAN.5.BP3: Analyse risks",
                    "MAN.5.BP4: Define and implement risk treatment",
                    "MAN.5.BP5: Monitor and communicate risks",
                ],
            },
            "MAN.6": {
                "name": "Measurement",
                "purpose": "The purpose of the Measurement Process is to collect, analyse and report "
                           "data relating to the products developed and processes implemented within the "
                           "project to support effective management of the processes and to demonstrate "
                           "the quality of the products.",
                "outcomes": [
                    "MAN.6.O1: A measurement strategy is developed",
                    "MAN.6.O2: Measurement objectives are identified",
                    "MAN.6.O3: An appropriate set of measures is identified",
                    "MAN.6.O4: Measurement activities are performed",
                    "MAN.6.O5: Measurement data are stored",
                    "MAN.6.O6: Measurement results are reported",
                ],
                "work_products": [
                    "08-16: Measurement Plan",
                    "15-09: Measurement Data",
                    "15-13: Process Performance Report",
                ],
                "base_practices": [
                    "MAN.6.BP1: Establish measurement objectives",
                    "MAN.6.BP2: Identify appropriate measures",
                    "MAN.6.BP3: Collect measurement data",
                    "MAN.6.BP4: Store measurement data",
                    "MAN.6.BP5: Analyse measurement data",
                    "MAN.6.BP6: Provide feedback",
                ],
            },
        },
    },
    "SUP": {
        "name": "Support",
        "processes": {
            "SUP.1": {
                "name": "Quality Assurance",
                "purpose": "The purpose of the Quality Assurance Process is to provide independent and "
                           "objective assurance that work products and processes comply with predefined "
                           "provisions and plans and that non-conformances are resolved.",
                "outcomes": [
                    "SUP.1.O1: A quality assurance strategy is developed",
                    "SUP.1.O2: Work products are evaluated objectively against applicable standards and requirements",
                    "SUP.1.O3: Processes are evaluated objectively",
                    "SUP.1.O4: Non-conformances are identified and communicated",
                    "SUP.1.O5: Non-conformances are resolved",
                    "SUP.1.O6: Management is kept informed of quality assurance activities",
                ],
                "work_products": [
                    "08-16: Quality Assurance Plan",
                    "08-14: Quality Record",
                ],
                "base_practices": [
                    "SUP.1.BP1: Develop quality assurance strategy",
                    "SUP.1.BP2: Evaluate work products",
                    "SUP.1.BP3: Evaluate process implementation",
                    "SUP.1.BP4: Communicate quality issues",
                    "SUP.1.BP5: Ensure resolution of non-conformances",
                    "SUP.1.BP6: Implement escalation mechanism",
                ],
            },
            "SUP.8": {
                "name": "Configuration Management",
                "purpose": "The purpose of the Configuration Management Process is to establish and "
                           "maintain the integrity of all the work products of a project or process "
                           "and make them available to concerned parties.",
                "outcomes": [
                    "SUP.8.O1: A configuration management strategy is developed",
                    "SUP.8.O2: Items to be controlled are identified",
                    "SUP.8.O3: Configuration items are controlled throughout their lifecycle",
                    "SUP.8.O4: Changes to the configuration items are controlled",
                    "SUP.8.O5: A status report of the configuration items is provided",
                    "SUP.8.O6: The completeness and consistency of configuration items is ensured",
                    "SUP.8.O7: Storage, handling and delivery of configuration items is controlled",
                ],
                "work_products": [
                    "08-16: Configuration Management Plan",
                    "11-06: Configuration Management Record",
                    "11-07: Change Request",
                ],
                "base_practices": [
                    "SUP.8.BP1: Develop configuration management strategy",
                    "SUP.8.BP2: Identify configuration items",
                    "SUP.8.BP3: Establish configuration management system",
                    "SUP.8.BP4: Control configuration items",
                    "SUP.8.BP5: Report configuration status",
                    "SUP.8.BP6: Verify and audit configuration item integrity",
                    "SUP.8.BP7: Manage the storage and delivery of configuration items",
                ],
            },
            "SUP.9": {
                "name": "Problem Resolution Management",
                "purpose": "The purpose of the Problem Resolution Management Process is to ensure that "
                           "problems are identified, analysed, managed and controlled to resolution.",
                "outcomes": [
                    "SUP.9.O1: A problem resolution management strategy is developed",
                    "SUP.9.O2: Problems are recorded and classified",
                    "SUP.9.O3: Problems are analysed and assessed for their impact",
                    "SUP.9.O4: Problem resolution is initiated",
                    "SUP.9.O5: Problems are tracked to closure",
                    "SUP.9.O6: The status of problems is communicated to affected parties",
                ],
                "work_products": [
                    "08-16: Problem Resolution Plan",
                    "13-16: Problem Report",
                ],
                "base_practices": [
                    "SUP.9.BP1: Prepare problem resolution management",
                    "SUP.9.BP2: Identify and record problems",
                    "SUP.9.BP3: Analyse and assess problems",
                    "SUP.9.BP4: Alert affected parties",
                    "SUP.9.BP5: Resolve problems",
                    "SUP.9.BP6: Track problems to closure",
                    "SUP.9.BP7: Analyse trends",
                ],
            },
            "SUP.10": {
                "name": "Change Request Management",
                "purpose": "The purpose of the Change Request Management Process is to ensure that change "
                           "requests are managed, tracked and implemented.",
                "outcomes": [
                    "SUP.10.O1: A change request management strategy is developed",
                    "SUP.10.O2: Requests for changes are recorded and identified",
                    "SUP.10.O3: Dependencies and relationships between change requests are identified",
                    "SUP.10.O4: Criteria for confirming and approving change requests are defined",
                    "SUP.10.O5: Changes are implemented, verified and tracked to closure",
                    "SUP.10.O6: Bidirectional traceability is established between change requests and affected work products",
                ],
                "work_products": [
                    "08-16: Change Request Management Plan",
                    "11-07: Change Request",
                    "13-19: Traceability Record",
                ],
                "base_practices": [
                    "SUP.10.BP1: Develop change request management strategy",
                    "SUP.10.BP2: Identify and record change requests",
                    "SUP.10.BP3: Analyse and assess change requests",
                    "SUP.10.BP4: Approve change requests before implementation",
                    "SUP.10.BP5: Review implementation of change requests",
                    "SUP.10.BP6: Track change requests to closure",
                    "SUP.10.BP7: Establish bidirectional traceability",
                ],
            },
        },
    },
    "ACQ": {
        "name": "Acquisition",
        "processes": {
            "ACQ.4": {
                "name": "Supplier Monitoring",
                "purpose": "The purpose of the Supplier Monitoring Process is to track and assess the "
                           "performance of the supplier against agreed requirements.",
                "outcomes": [
                    "ACQ.4.O1: A supplier monitoring strategy is developed",
                    "ACQ.4.O2: Technical progress of the supplier is monitored against agreed requirements",
                    "ACQ.4.O3: The quality of the supplier's work products is monitored against agreed requirements",
                    "ACQ.4.O4: Risks in the supplier relationship are identified and tracked",
                ],
                "work_products": [
                    "08-16: Supplier Monitoring Plan",
                    "15-13: Supplier Performance Report",
                ],
                "base_practices": [
                    "ACQ.4.BP1: Develop supplier monitoring strategy",
                    "ACQ.4.BP2: Review technical development with supplier",
                    "ACQ.4.BP3: Monitor supplier's risk management",
                    "ACQ.4.BP4: Conduct reviews of supplier work products",
                    "ACQ.4.BP5: Communicate results of supplier monitoring",
                ],
            },
        },
    },
}

# Rating scale definitions
RATING_SCALE = {
    "N": {"name": "Not achieved", "range": "0-15%", "score": 0},
    "P": {"name": "Partially achieved", "range": "15-50%", "score": 1},
    "L": {"name": "Largely achieved", "range": "50-85%", "score": 2},
    "F": {"name": "Fully achieved", "range": "85-100%", "score": 3},
}

# Capability level determination rules (ISO/IEC 33020)
LEVEL_ACHIEVEMENT_RULES = {
    1: {"required_ratings": {"PA 1.1": ["F"]}},
    2: {
        "required_ratings": {
            "PA 1.1": ["F", "L"],
            "PA 2.1": ["F"],
            "PA 2.2": ["F"],
        }
    },
    3: {
        "required_ratings": {
            "PA 1.1": ["F", "L"],
            "PA 2.1": ["F", "L"],
            "PA 2.2": ["F", "L"],
            "PA 3.1": ["F"],
            "PA 3.2": ["F"],
        }
    },
    4: {
        "required_ratings": {
            "PA 1.1": ["F", "L"],
            "PA 2.1": ["F", "L"],
            "PA 2.2": ["F", "L"],
            "PA 3.1": ["F", "L"],
            "PA 3.2": ["F", "L"],
            "PA 4.1": ["F"],
            "PA 4.2": ["F"],
        }
    },
    5: {
        "required_ratings": {
            "PA 1.1": ["F", "L"],
            "PA 2.1": ["F", "L"],
            "PA 2.2": ["F", "L"],
            "PA 3.1": ["F", "L"],
            "PA 3.2": ["F", "L"],
            "PA 4.1": ["F", "L"],
            "PA 4.2": ["F", "L"],
            "PA 5.1": ["F"],
            "PA 5.2": ["F"],
        }
    },
}

# Common ASPICE assessment questions for each capability level PA
ASSESSMENT_QUESTIONS = {
    "PA 1.1": [
        "Are the process outcomes defined and achieved?",
        "Are the base practices of the process performed?",
        "Are the required work products produced and available?",
        "Is there evidence that the process purpose is being met?",
        "Are all mandatory base practices implemented?",
    ],
    "PA 2.1": [
        "Are objectives for the performance of the process identified?",
        "Is the performance of the process planned?",
        "Is the performance of the process monitored against the plan?",
        "Are adjustments made when performance deviates from plan?",
        "Are responsibilities and authorities for performing the process defined and communicated?",
        "Are personnel performing the process appropriately prepared?",
        "Are resources (human, infrastructure) necessary for performing the process identified and made available?",
        "Are the interfaces between the involved parties managed?",
    ],
    "PA 2.2": [
        "Are requirements for the work products of the process defined?",
        "Are requirements for documentation and control of work products defined?",
        "Are work products appropriately identified, documented and controlled?",
        "Are work products reviewed in accordance with planned arrangements and issues resolved?",
    ],
    "PA 3.1": [
        "Is a standard process defined and maintained?",
        "Are tailoring guidelines available for adapting the standard process?",
        "Is the sequence and interaction of the standard process with other processes determined?",
        "Are required competencies and roles identified for performing the standard process?",
        "Is required infrastructure and work environment identified for performing the standard process?",
        "Are methods to monitor the effectiveness and suitability of the standard process determined?",
    ],
    "PA 3.2": [
        "Is a defined process deployed based on an appropriately selected and/or tailored standard process?",
        "Are required roles, responsibilities and authorities assigned for performing the defined process?",
        "Are personnel performing the defined process competent?",
        "Are required resources available for performing the defined process?",
        "Is the infrastructure and work environment available for performing the defined process?",
        "Are appropriate data collected and analysed to demonstrate the suitability and effectiveness of the process?",
    ],
    "PA 4.1": [
        "Are process information needs identified in support of relevant quality and process performance objectives?",
        "Are process measurement objectives derived from process information needs?",
        "Are quantitative objectives for process performance established?",
        "Are measures and frequency of measurement identified and applied?",
        "Are measurement results collected, analysed and reported to characterise process performance?",
    ],
    "PA 4.2": [
        "Are analysis techniques used to identify special causes of variation in process performance?",
        "Are corrective actions taken to address root causes of special cause variation?",
        "Are control limits established for normal process performance?",
        "Is measurement data analysed for special causes of process variation?",
        "Are corrective actions taken when control limits are exceeded?",
    ],
    "PA 5.1": [
        "Are process improvement objectives defined that support relevant business goals?",
        "Is data analysed to identify common causes of variations in process performance?",
        "Is data analysed to identify opportunities for best practice and innovation?",
        "Are improvement opportunities from new technologies and process concepts identified?",
        "Is an implementation strategy derived to achieve process improvement objectives?",
    ],
    "PA 5.2": [
        "Is the impact of all proposed changes assessed against the objectives of the defined and standard process?",
        "Is implementation of agreed changes managed to ensure disruption to process performance is understood and controlled?",
        "Is the effectiveness of process change evaluated against defined product requirements and process objectives?",
    ],
}
