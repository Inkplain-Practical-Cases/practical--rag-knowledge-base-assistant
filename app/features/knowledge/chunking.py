# Keep source and chunk identity for every citation.
def service_chunk_documents(documents:list[dict],size:int=90)->list[dict]:
    chunks=[]
    for doc in documents:
        words=doc["text"].split()
        for i,start in enumerate(range(0,len(words),size)):
            chunks.append({"id":f'{doc["id"]}-c{i+1}',"source_id":doc["id"],"title":doc["title"],"text":" ".join(words[start:start+size])})
    return chunks
