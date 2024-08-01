# from typing import List, Dict, Any, Optional
# from dataclasses import dataclass
# from pinecone import Pinecone, ServerlessSpec, QueryResponse, UpsertResponse, Vector
# from src.config.config import Config
# from src.repository.embeddings import Embeddings


# @dataclass
# class Message:
#     id: str
#     text: str
#     timestamp: str
#     sender_id: str
#     sender_type: str
#     sender_name: str = ""
#     sender_first_name: str = ""
#     sender_last_name: str = ""


# @dataclass
# class Messages:
#     messages: List[Message]


# @dataclass
# class HistoryResponse:
#     id: str
#     metadata: Message
#     score: float
#     values: List[float]


# class HistoryEngine:
#     def __init__(self, cfg: Config, embedder: Embeddings):
#         self.cfg = cfg
#         self.pc = Pinecone(api_key=self.cfg.PINECONE_API_KEY)
#         name = "history"
#         self.__create_index(
#             name=name,
#             dimension=1536,
#             metric="cosine",
#             spec=ServerlessSpec(cloud="aws", region="us-east-1"),
#         )
#         self.index = self.pc.Index(name=name)
#         self.embedder = embedder

#     def __create_index(self, name, dimension, metric, spec) -> None:
#         if name not in self.pc.list_indexes().names():
#             self.pc.create_index(
#                 name=name,
#                 dimension=dimension,
#                 metric=metric,
#                 spec=spec,
#             )
#         else:
#             print(f"Index {name} already exists")

#     def upsert_history(
#         self, messages: List[types.Message], namespace: str
#     ) -> UpsertResponse:
#         mes = [
#             Message(
#                 id=str(m.message_id),
#                 text=m.text,  # type: ignore
#                 timestamp=str(m.date),
#                 sender_id=str(m.from_user.id),
#                 sender_type="user" if not m.from_user.is_bot else "bot",
#                 sender_name=m.from_user.username if m.from_user.username else "",
#                 sender_first_name=(
#                     m.from_user.first_name if m.from_user.first_name else ""
#                 ),
#                 sender_last_name=m.from_user.last_name if m.from_user.last_name else "",
#             )
#             for m in messages
#         ]
#         mess = Messages(messages=mes)
#         messages_texts = [message.text for message in mess.messages]
#         vecs = self.embedder.embed_documents(messages_texts)
#         vectors = [
#             Vector(
#                 id=message.id,
#                 values=vec,
#                 metadata=vars(
#                     message
#                 ),  # Fucking dataclasses magic of serialization to dict
#             )
#             for message, vec in zip(mess.messages, vecs)
#         ]
#         res = self.index.upsert(vectors=vectors, namespace=namespace)  # type: ignore
#         return res

#     def get_relevancy_history(
#         self, message: types.Message, namespace: str, top_k: int
#     ) -> List[Optional[HistoryResponse]]:
#         vector = self.embedder.embed_query(message.text)  # type: ignore
#         responses = self.index.query(
#             vector=vector,
#             namespace=namespace,
#             top_k=top_k,
#             include_values=False,
#             include_metadata=True,
#         )

#         resp: List[Optional[HistoryResponse]] = [
#             HistoryResponse(
#                 id=r.get("id"),
#                 metadata=Message(**r.metadata),
#                 score=r.get("score"),
#                 values=r.get("values"),
#             )
#             for r in responses.get("matches")
#         ]
#         return resp

#     def get_last_messages(
#         self, message: types.Message, namespace: str, top_k: int
#     ) -> List[Optional[HistoryResponse]]:
#         ids = [str(message.message_id - i) for i in range(top_k)]
#         responses = self.index.fetch(ids, namespace=namespace)
#         print(responses)

#         res = responses.get("vectors")
#         ids = res.keys()

#         resp: List[Optional[HistoryResponse]] = [
#             HistoryResponse(
#                 id=r.get("id"), metadata=Message(**r.metadata), score=0, values=[]
#             )
#             for r in res.values()
#         ]
#         # order resp by id
#         resp = sorted(resp, key=lambda x: int(x.id))  # type: ignore

#         return resp

#     def delete_history(self, namespace: str) -> Dict[str, Any]:
#         res = self.index.delete(namespace=namespace, delete_all=True)
#         return res
