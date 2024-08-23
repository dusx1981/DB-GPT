"""Import all models to make sure they are registered with SQLAlchemy.
"""

from dbgpt.app.knowledge.chunk_db import DocumentChunkEntity
from dbgpt.app.knowledge.document_db import KnowledgeDocumentEntity
from dbgpt.app.openapi.api_v1.feedback.feed_back_db import ChatFeedBackEntity
from dbgpt.datasource.manages.connect_config_db import ConnectConfigEntity
from dbgpt.model.cluster.registry_impl.db_storage import ModelInstanceEntity
from dbgpt.serve.agent.app.recommend_question.recommend_question import (
    RecommendQuestionEntity,
)
from dbgpt.serve.agent.hub.db.my_plugin_db import MyPluginEntity
from dbgpt.serve.agent.hub.db.plugin_hub_db import PluginHubEntity
from dbgpt.serve.file.models.models import ServeEntity as FileServeEntity
from dbgpt.serve.flow.models.models import ServeEntity as FlowServeEntity
from dbgpt.serve.flow.models.models import VariablesEntity as FlowVariableEntity
from dbgpt.serve.prompt.models.models import ServeEntity as PromptManageEntity
from dbgpt.serve.rag.models.models import KnowledgeSpaceEntity
from dbgpt.storage.chat_history.chat_history_db import (
    ChatHistoryEntity,
    ChatHistoryMessageEntity,
)

_MODELS = [
    PluginHubEntity,
    FileServeEntity,
    MyPluginEntity,
    PromptManageEntity,
    KnowledgeSpaceEntity,
    KnowledgeDocumentEntity,
    DocumentChunkEntity,
    ChatFeedBackEntity,
    ConnectConfigEntity,
    ChatHistoryEntity,
    ChatHistoryMessageEntity,
    ModelInstanceEntity,
    FlowServeEntity,
    RecommendQuestionEntity,
    FlowVariableEntity,
]
