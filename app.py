
import streamlit as st
import sys
import json
import traceback
from pathlib import Path

# ============================================================
# 1. PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Software Engineering Platform",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)



PROJECT_ROOT = Path(__file__).resolve().parent
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

# ============================================================
# 2. CUSTOM STYLING
# ============================================================


# ============================================================
# PREMIUM AI DEVELOPER WORKSPACE - DESIGN SYSTEM V2
# ============================================================

st.markdown("""
<style>

:root {
    color-scheme: dark;
    --bg: #080D19;
    --panel: #111A2D;
    --panel2: #151F35;
    --line: #283650;
    --purple: #9672FF;
    --blue: #4D8DFF;
    --cyan: #54D6E8;
    --text: #F2F5FF;
    --muted: #9BAAC4;
}

.stApp {
    background:
        radial-gradient(ellipse at 12% 0%,
            rgba(110, 70, 220, 0.17), transparent 35%),
        radial-gradient(ellipse at 95% 20%,
            rgba(45, 115, 220, 0.11), transparent 32%),
        linear-gradient(145deg, #080D19, #0D1526 55%, #080D19);
    color: var(--text);
}

[data-testid="stMain"] {
    background: transparent;
}

[data-testid="stMainBlockContainer"] {
    max-width: 1500px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

[data-testid="stHeader"] {
    background: rgba(8, 13, 25, 0.82);
}

[data-testid="stSidebar"] {
    min-width: 285px;
    width: 285px;
    background: linear-gradient(180deg, #10182B, #090F1D);
    border-right: 1px solid #26334D;
}

[data-testid="stSidebar"] > div {
    background: transparent;
}

[data-testid="stSidebar"] hr {
    border-color: #283650;
    margin: 1.1rem 0;
}

[data-testid="stSidebar"] p {
    color: #A9B8D0;
}

h1, h2, h3, h4 {
    color: #F2F5FF !important;
    letter-spacing: -0.5px;
}

p, label, li {
    color: #D0D9EA;
    line-height: 1.65;
}

[data-testid="stCaptionContainer"] {
    color: var(--muted);
}

.sidebar-brand {
    padding: 18px 12px;
    text-align: center;
    border: 1px solid #34436B;
    border-radius: 17px;
    background: linear-gradient(140deg,
        rgba(123, 83, 225, .19),
        rgba(48, 104, 200, .10));
    box-shadow: 0 0 25px rgba(117, 83, 220, .09);
}

.sidebar-brand .brand-icon {
    font-size: 36px;
    margin-bottom: 5px;
}

.sidebar-brand .brand-title {
    color: #F5F2FF;
    font-size: 18px;
    font-weight: 850;
    letter-spacing: 1.5px;
}

.sidebar-brand .brand-subtitle {
    color: #A9B8D0;
    font-size: 10px;
    letter-spacing: 2px;
    margin-top: 5px;
}

.sidebar-section {
    color: #8F9DB7;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.8px;
    margin: 17px 0 8px;
}

[data-testid="stRadio"] label {
    color: #E1E8F6 !important;
    font-weight: 600;
}

[data-testid="stRadio"] > div {
    gap: 9px;
}

[data-testid="stRadio"] > div > label {
    background: rgba(24, 36, 60, .65);
    border: 1px solid #2C3B58;
    border-radius: 11px;
    padding: 10px 12px;
}

[data-testid="stRadio"] > div > label:has(
    input:checked
) {
    background: linear-gradient(100deg,
        rgba(113, 78, 211, .28),
        rgba(52, 104, 205, .20));
    border-color: #826AE0;
}

.hero-kicker {
    color: #A88CFF;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 2.5px;
    margin-bottom: 8px;
}

.hero-title {
    color: #F5F6FF;
    font-size: clamp(29px, 4vw, 43px);
    line-height: 1.12;
    font-weight: 850;
    letter-spacing: -1.5px;
}

.hero-description {
    color: #A8B6CF;
    font-size: 14px;
    margin-top: 10px;
    max-width: 780px;
    line-height: 1.7;
}

.status-pill {
    display: inline-block;
    padding: 6px 11px;
    border: 1px solid #345B61;
    background: rgba(35, 160, 139, .10);
    color: #75E1C6;
    border-radius: 20px;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1px;
}

.agent-card {
    min-height: 137px;
    padding: 17px 14px;
    border: 1px solid #2B3B59;
    border-radius: 15px;
    background: linear-gradient(145deg,
        rgba(25, 37, 62, .96),
        rgba(15, 24, 42, .96));
    box-shadow: 0 8px 25px rgba(0,0,0,.13);
    transition: .2s ease;
}

.agent-card:hover {
    border-color: #8872E8;
    transform: translateY(-2px);
    box-shadow: 0 8px 28px rgba(112, 84, 218, .15);
}

.agent-icon {
    font-size: 25px;
    margin-bottom: 9px;
}

.agent-name {
    color: #F0F2FF;
    font-weight: 800;
    font-size: 12px;
    letter-spacing: 1px;
}

.agent-description {
    color: #A4B2C9;
    font-size: 11px;
    margin-top: 7px;
    line-height: 1.5;
}

.workspace-panel {
    border: 1px solid #2B3B58;
    border-radius: 16px;
    padding: 18px;
    background: linear-gradient(145deg,
        rgba(20, 31, 52, .94),
        rgba(14, 23, 40, .94));
    margin-bottom: 15px;
}

.section-eyebrow {
    color: #A78BFA;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.8px;
}

.stButton > button {
    min-height: 44px;
    border-radius: 11px;
    font-weight: 700;
    transition: all .2s ease;
}

.stButton > button[kind="primary"] {
    background: linear-gradient(105deg, #7650E8, #3978E8);
    color: white;
    border: 1px solid #9278F5;
    box-shadow: 0 5px 20px rgba(93, 78, 220, .22);
}

.stButton > button[kind="primary"]:hover {
    filter: brightness(1.13);
    box-shadow: 0 5px 25px rgba(93, 78, 220, .35);
    transform: translateY(-1px);
}

.stButton > button[kind="secondary"] {
    background: #17243B;
    color: #E2EAF9;
    border: 1px solid #344765;
}

.stTextInput input,
.stTextArea textarea,
[data-baseweb="input"] input {
    background: #0E192C !important;
    color: #F3F6FF !important;
    border: 1px solid #354664 !important;
    border-radius: 11px !important;
}

.stTextArea textarea:focus,
.stTextInput input:focus {
    border-color: #9672FF !important;
    box-shadow: 0 0 0 1px #9672FF !important;
}

[data-baseweb="select"] > div {
    background: #111D32 !important;
    border: 1px solid #354664 !important;
    border-radius: 10px !important;
    color: white !important;
}

[data-testid="stMetric"] {
    background: linear-gradient(145deg, #192640, #111B2F);
    border: 1px solid #30415F;
    border-radius: 14px;
    padding: 15px;
}

[data-testid="stMetricLabel"] {
    color: #AAB9D1 !important;
}

[data-testid="stMetricValue"] {
    color: #F2F5FF !important;
}

.stTabs [data-baseweb="tab-list"] {
    gap: 7px;
    padding: 7px;
    background: #101A2D;
    border: 1px solid #293A57;
    border-radius: 13px;
}

.stTabs [data-baseweb="tab"] {
    color: #AEBBD1;
    border-radius: 9px;
    padding: 10px 14px;
}

.stTabs [aria-selected="true"] {
    background: #302750 !important;
    color: #D5C9FF !important;
    border-bottom: 2px solid #A78BFA !important;
}

[data-testid="stExpander"] {
    background: #111B2F;
    border: 1px solid #2B3B58;
    border-radius: 12px;
}

[data-testid="stChatMessage"] {
    background: rgba(21, 33, 55, .93);
    border: 1px solid #30415E;
    border-radius: 15px;
    padding: 14px;
    margin-bottom: 12px;
}

[data-testid="stChatInput"] {
    background: #101B2F;
    border: 1px solid #3B4D6C;
    border-radius: 13px;
}

[data-testid="stAlert"] {
    border-radius: 12px;
}

hr {
    border-color: #293A57;
}

footer {
    visibility: hidden;
}

::-webkit-scrollbar {
    width: 7px;
}

::-webkit-scrollbar-thumb {
    background: #435574;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)


# 3. LOAD MULTI-AGENT COORDINATOR
# ============================================================

@st.cache_resource
def load_coordinator():

    from multi_agent_coordinator import MultiAgentCoordinator

    try:
        groq_api_key = st.secrets.get("GROQ_API_KEY")
    except Exception:
        groq_api_key = None

    llm_provider = "groq" if groq_api_key else "ollama"

    return MultiAgentCoordinator(
        project_root=str(PROJECT_ROOT),
        model_name="qwen2.5:3b",
        llm_provider=llm_provider,
        groq_api_key=groq_api_key,
        groq_model="openai/gpt-oss-20b"
    )

# ============================================================
# 4. SESSION STATE
# ============================================================

if "general_messages" not in st.session_state:
    st.session_state.general_messages = []

if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None

# ============================================================
# 5. SIDEBAR - APPLICATION SELECTION
# ============================================================


# ============================================================
# PREMIUM AI PLATFORM SIDEBAR
# ============================================================

st.sidebar.markdown("""
<div class="sidebar-brand">
    <div class="brand-icon">✦</div>
    <div class="brand-title">NEXUS AI</div>
    <div class="brand-subtitle">INTELLIGENT DEVELOPER WORKSPACE</div>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown(
    '<div class="sidebar-section">WORKSPACE NAVIGATION</div>',
    unsafe_allow_html=True
)

mode = st.sidebar.radio(
    "Choose your workspace",
    [
        "🤖 General AI Assistant",
        "💻 Software Engineering Agent"
    ],
    index=0,
    key="application_mode",
    label_visibility="collapsed"
)

st.sidebar.markdown("---")

if mode == "🤖 General AI Assistant":
    st.sidebar.markdown("### ✨ General AI")
    st.sidebar.caption(
        "Your conversational AI space for learning, "
        "programming and exploring ideas."
    )

    st.sidebar.markdown("**Explore topics**")
    st.sidebar.markdown(
        "- Python and programming\n"
        "- Artificial Intelligence\n"
        "- Machine Learning\n"
        "- Data Science\n"
        "- SQL and databases"
    )

else:
    st.sidebar.markdown("### ⚡ Engineering AI")
    st.sidebar.caption(
        "A coordinated team of AI agents for source-code intelligence."
    )

    st.sidebar.markdown("**Integrated agent system**")
    st.sidebar.markdown(
        "- 🔍 Retrieval Agent\n"
        "- 📝 Code Review Agent\n"
        "- 🛡️ Security Agent\n"
        "- 🧪 Testing Agent"
    )

st.sidebar.markdown("---")

st.sidebar.markdown(
    '<div class="sidebar-section">LOCAL AI ENGINE</div>',
    unsafe_allow_html=True
)

st.sidebar.markdown("**◉ Ollama Runtime**")
st.sidebar.caption("Model: Qwen 2.5 · 3B")
st.sidebar.caption("Local model integration")


# 6. GENERAL AI ASSISTANT
# ============================================================


if mode == "🤖 General AI Assistant":

    st.markdown("""
    <div class="hero-kicker">NEXUS AI / CONVERSATIONAL INTELLIGENCE</div>
    <div class="hero-title">Your AI thinking space.</div>
    <div class="hero-description">
        Ask questions, explore ideas, learn programming and solve
        problems with your local AI assistant.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("")

    header_left, header_right = st.columns([4, 1])

    with header_left:
        st.markdown(
            '<span class="status-pill">● LOCAL AI ENGINE</span>',
            unsafe_allow_html=True
        )

    with header_right:
        if st.button(
            "＋ New chat",
            use_container_width=True,
            key="clear_general_chat"
        ):
            st.session_state.general_messages = []
            st.rerun()

    st.markdown("---")

    # Empty conversation welcome screen
    if not st.session_state.general_messages:
        st.markdown("""
        <div class="workspace-panel">
            <div style="font-size:34px;">✦</div>
            <h3 style="margin-bottom:5px;">What would you like to explore?</h3>
            <p style="color:#A9B8D0;">
                Start a conversation with your AI assistant.
                Ask a technical question or request a step-by-step explanation.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("#### Suggested conversation starters")

        suggestions = st.columns(2)

        suggestion_cards = [
            ("🐍", "Python", "Explain Python decorators with examples."),
            ("🧠", "Artificial Intelligence",
             "Explain how large language models work."),
            ("📊", "Data Science",
             "Explain the difference between classification and regression."),
            ("💻", "Programming",
             "Write a Python program to analyze a CSV file.")
        ]

        for column, (emoji, title, description) in zip(
            suggestions, suggestion_cards
        ):
            with column:
                st.markdown(
                    f"""
                    <div class="agent-card" style="min-height:105px;">
                        <div class="agent-name">{emoji} {title}</div>
                        <div class="agent-description">{description}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    # Display conversation history
    for message in st.session_state.general_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_prompt = st.chat_input(
        "Message Nexus AI... Ask anything."
    )

    if user_prompt:

        st.session_state.general_messages.append({
            "role": "user",
            "content": user_prompt
        })

        with st.chat_message("user"):
            st.markdown(user_prompt)

        with st.chat_message("assistant"):
            try:
                with st.spinner("Nexus AI is thinking..."):

                    recent_messages = (
                        st.session_state.general_messages[-10:]
                    )

                    conversation = ""

                    for message in recent_messages:
                        conversation += (
                            f"{message['role'].upper()}: "
                            f"{message['content']}\n"
                        )

                    prompt = f"""
You are a helpful general AI assistant.

Explain concepts in beginner-friendly language.
Use practical examples.
For programming questions, provide working code.
Explain code step by step when useful.
Maintain the conversation context.
Do not invent facts.

Conversation:
{conversation}

Assistant:
"""

                    coordinator = load_coordinator()
                    answer = coordinator._ask_llm(prompt)

                    if not answer:
                        answer = (
                            "I could not generate an answer. "
                            "Please try again."
                        )

                    st.markdown(answer)

                st.session_state.general_messages.append({
                    "role": "assistant",
                    "content": answer
                })

            except Exception as error:
                st.error(f"Assistant error: {error}")



# 7. SOFTWARE ENGINEERING AGENT
# ============================================================


elif mode == "💻 Software Engineering Agent":

    st.markdown("""
    <div class="hero-kicker">NEXUS AI / SOFTWARE ENGINEERING INTELLIGENCE</div>
    <div class="hero-title">Code Intelligence Workspace.</div>
    <div class="hero-description">
        Four specialized AI agents work together to retrieve source code,
        understand program behavior, inspect security patterns and
        validate software through tests.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("")

    st.markdown(
        '<span class="status-pill">● MULTI-AGENT SYSTEM AVAILABLE</span>',
        unsafe_allow_html=True
    )

    st.markdown("")
    st.markdown("#### Your AI engineering team")

    agent_columns = st.columns(4)

    agent_cards = [
        ("🔍", "RETRIEVAL AGENT",
         "Find relevant code and source evidence."),
        ("🧠", "CODE REVIEW AGENT",
         "Understand functions, logic and behavior."),
        ("🛡️", "SECURITY AGENT",
         "Inspect potential security concerns."),
        ("🧪", "TESTING AGENT",
         "Generate and validate test scenarios.")
    ]

    for column, (emoji, name, description) in zip(
        agent_columns, agent_cards
    ):
        with column:
            st.markdown(
                f"""
                <div class="agent-card">
                    <div class="agent-icon">{emoji}</div>
                    <div class="agent-name">{name}</div>
                    <div class="agent-description">{description}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("")

    # Repository configuration
    with st.container(border=True):

        st.markdown(
            '<div class="section-eyebrow">01 / PROJECT CONFIGURATION</div>',
            unsafe_allow_html=True
        )

        st.markdown("### Connect to a code repository")

        st.caption(
            "Select one of the indexed repositories and configure "
            "how much source code the retrieval agent should inspect."
        )

        repositories = [
            "black",
            "click",
            "fastapi",
            "flask",
            "httpx",
            "pydantic",
            "pytest",
            "requests",
            "rich",
            "typer"
        ]

        config_col1, config_col2 = st.columns([1.5, 1])

        with config_col1:
            repository = st.selectbox(
                "Source repository",
                repositories,
                index=repositories.index("requests")
            )

        with config_col2:
            top_k = st.slider(
                "Retrieval depth",
                min_value=1,
                max_value=10,
                value=5,
                help="Number of relevant code chunks to retrieve."
            )

    st.markdown("")

    # AI engineering prompt workspace
    with st.container(border=True):

        st.markdown(
            '<div class="section-eyebrow">02 / AI ENGINEERING PROMPT</div>',
            unsafe_allow_html=True
        )

        st.markdown("### What should the agents investigate?")

        st.caption(
            "Describe the function, code behavior, engineering question "
            "or issue you want the multi-agent system to analyze."
        )

        query = st.text_area(
            "Engineering question",
            placeholder=(
                "Example: Explain how requests.get() delegates "
                "to request(). Trace the execution flow and "
                "identify the relevant source functions."
            ),
            height=145,
            label_visibility="collapsed",
            key="engineering_query"
        )

        st.markdown("")

        run_analysis = st.button(
            "✦  EXECUTE MULTI-AGENT ANALYSIS",
            type="primary",
            use_container_width=True,
            key="execute_multi_agent_analysis"
        )

    st.markdown("")

    st.caption(
        "Execution pipeline: Retrieval → Code Review → Security → Testing"
    )



    # Run all four agents
    # --------------------------------------------------------

    if run_analysis:

        if not query.strip():

            st.warning("Please enter a question first.")

        else:

            st.session_state.analysis_result = None

            try:

                with st.spinner(
                    "Running all four AI agents. Please wait..."
                ):

                    coordinator = load_coordinator()

                    result = coordinator.run(
                        query=query,
                        top_k=top_k,
                        repository=repository
                    )

                    st.session_state.analysis_result = result

                if isinstance(result, dict):

                    if result.get("overall_status") == "completed":
                        st.success("Multi-agent analysis completed.")

                    else:
                        st.warning(
                            "Analysis completed with warnings. "
                            "Inspect individual agent results."
                        )

                else:
                    st.warning(
                        "Coordinator returned an unexpected result."
                    )

            except Exception as error:

                st.error(f"Multi-agent analysis failed: {error}")
                st.code(traceback.format_exc())

    # ========================================================
    # 8. DISPLAY AGENT RESULTS
    # ========================================================

    result = st.session_state.analysis_result

    if result is not None:

        st.markdown("---")
        st.markdown("## 📊 Multi-Agent Analysis Results")

        if not isinstance(result, dict):

            st.warning("Unexpected result format.")
            st.write(result)

        else:

            # IMPORTANT:
            # The coordinator stores all four agents under "agents".

            agents = result.get("agents", {})

            if not agents:

                st.error("No agent results found in coordinator output.")

                with st.expander("Inspect raw coordinator response"):
                    st.json(result)

            else:

                # ------------------------------------------------
                # Overall status
                # ------------------------------------------------

                overall_status = result.get(
                    "overall_status",
                    "unknown"
                )

                st.info(
                    f"Overall Status: {overall_status.upper()}"
                )

                st.write(
                    "**Repository:**",
                    result.get("repository_filter", "Not specified")
                )

                st.write(
                    "**Query:**",
                    result.get("query", "")
                )

                # ------------------------------------------------
                # Agent status summary
                # ------------------------------------------------

                st.markdown("### Agent Execution Summary")

                summary_columns = st.columns(4)

                agent_information = [
                    ("retrieval", "🔍 Retrieval"),
                    ("code_review", "📝 Code Review"),
                    ("security", "🛡️ Security"),
                    ("testing", "🧪 Testing")
                ]

                for column, (key, label) in zip(
                    summary_columns,
                    agent_information
                ):

                    agent_data = agents.get(key, {})

                    status = agent_data.get(
                        "status",
                        "missing"
                    )

                    with column:

                        st.metric(
                            label,
                            str(status).upper()
                        )

                st.markdown("---")

                # ------------------------------------------------
                # Four independent tabs
                # ------------------------------------------------

                retrieval_tab, review_tab, security_tab, testing_tab = (
                    st.tabs([
                        "🔍 Retrieval",
                        "📝 Code Review",
                        "🛡️ Security",
                        "🧪 Testing"
                    ])
                )

                # =================================================
                # AGENT 1 - RETRIEVAL
                # =================================================

                with retrieval_tab:

                    st.subheader("🔍 Retrieval Agent")

                    retrieval = agents.get(
                        "retrieval",
                        {}
                    )

                    st.write(
                        "**Status:**",
                        retrieval.get("status", "unknown")
                    )

                    st.metric(
                        "Retrieved Code Chunks",
                        retrieval.get("results_count", 0)
                    )

                    retrieved_results = retrieval.get(
                        "results",
                        []
                    )

                    if retrieved_results:

                        st.markdown("### Retrieved Source Code")

                        for index, item in enumerate(
                            retrieved_results,
                            start=1
                        ):

                            with st.expander(
                                f"Code Chunk {index}"
                            ):

                                st.json(item)

                    else:

                        st.warning(
                            "No code chunks were retrieved."
                        )

                    if retrieval.get("error"):
                        st.error(retrieval["error"])

                # =================================================
                # AGENT 2 - CODE REVIEW
                # =================================================

                with review_tab:

                    st.subheader("📝 Code Review Agent")

                    review = agents.get(
                        "code_review",
                        {}
                    )

                    st.write(
                        "**Status:**",
                        review.get("status", "unknown")
                    )

                    if review.get("error"):
                        st.error(review["error"])

                    # Show all actual fields returned by the agent.
                    # This avoids assuming a particular output schema.

                    review_content = {
                        key: value
                        for key, value in review.items()
                        if key not in {"status", "error"}
                    }

                    if review_content:

                        for key, value in review_content.items():

                            st.markdown(
                                f"### {key.replace('_', ' ').title()}"
                            )

                            if isinstance(value, str):
                                st.markdown(value)

                            elif isinstance(value, (dict, list)):
                                st.json(value)

                            else:
                                st.write(value)

                    elif not review.get("error"):

                        st.warning(
                            "The code review agent returned no "
                            "additional output fields."
                        )

                    with st.expander(
                        "View Complete Code Review Response"
                    ):

                        st.json(review)

                # =================================================
                # AGENT 3 - SECURITY
                # =================================================

                with security_tab:

                    st.subheader("🛡️ Security Agent")

                    security = agents.get(
                        "security",
                        {}
                    )

                    st.write(
                        "**Status:**",
                        security.get("status", "unknown")
                    )

                    if "new_scan_performed" in security:

                        st.write(
                            "**Fresh scan performed:**",
                            security["new_scan_performed"]
                        )

                    if security.get("error"):
                        st.error(security["error"])

                    # Display every field actually returned.

                    security_content = {
                        key: value
                        for key, value in security.items()
                        if key not in {"status", "error"}
                    }

                    if security_content:

                        for key, value in security_content.items():

                            st.markdown(
                                f"### {key.replace('_', ' ').title()}"
                            )

                            if isinstance(value, str):
                                st.markdown(value)

                            elif isinstance(value, (dict, list)):
                                st.json(value)

                            else:
                                st.write(value)

                    else:

                        st.warning(
                            "No additional security output was returned."
                        )

                    with st.expander(
                        "View Complete Security Response"
                    ):

                        st.json(security)

                # =================================================
                # AGENT 4 - TESTING
                # =================================================

                with testing_tab:

                    st.subheader("🧪 Testing Agent")

                    testing = agents.get(
                        "testing",
                        {}
                    )

                    st.write(
                        "**Status:**",
                        testing.get("status", "unknown")
                    )

                    if testing.get("error"):
                        st.error(testing["error"])

                    # Display every actual field returned.

                    testing_content = {
                        key: value
                        for key, value in testing.items()
                        if key not in {"status", "error"}
                    }

                    if testing_content:

                        for key, value in testing_content.items():

                            st.markdown(
                                f"### {key.replace('_', ' ').title()}"
                            )

                            if isinstance(value, str):
                                st.markdown(value)

                            elif isinstance(value, (dict, list)):
                                st.json(value)

                            else:
                                st.write(value)

                    else:

                        st.warning(
                            "No additional testing output was returned."
                        )

                    with st.expander(
                        "View Complete Testing Response"
                    ):

                        st.json(testing)

                # ------------------------------------------------
                # Complete result
                # ------------------------------------------------

                with st.expander(
                    "📄 View Complete Multi-Agent Output"
                ):

                    st.json(result)

                # ------------------------------------------------
                # Limitations
                # ------------------------------------------------

                limitations = result.get(
                    "limitations",
                    []
                )

                if limitations:

                    with st.expander(
                        "⚠️ Analysis Limitations"
                    ):

                        for limitation in limitations:
                            st.markdown(f"- {limitation}")

# ============================================================
# 9. FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "AI Software Engineering Platform | "
    "General AI Assistant + Multi-Agent Software Engineering Agent | "
    "Ollama + Qwen 2.5"
)



# ============================================================
