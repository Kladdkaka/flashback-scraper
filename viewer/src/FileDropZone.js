import styled from "styled-components/macro";
import React, {useCallback} from "react";
import {useDropzone} from "react-dropzone";

const DropZoneDiv = styled.div`
  flex-grow: 1;
  justify-content: center;
  align-items: center;
  display: flex;
`

function FileDropZone({onResult}) {
  const onDrop = useCallback(acceptedFiles => {
    const [file] = acceptedFiles

    const reader = new FileReader()

    reader.onabort = () => console.log('file reading was aborted')
    reader.onerror = () => console.log('file reading has failed')
    reader.onload = () => {
      const text = reader.result

      console.log(text)

      const entries = text.split('\n').map(line => line.trim()).filter(line => line.length > 0).map(JSON.parse)

      console.log(entries)

      onResult(entries)
    }
    reader.readAsText(file, 'utf-8')
  }, [])

  const {getRootProps, getInputProps, isDragActive} = useDropzone({onDrop})

  return (
    <DropZoneDiv {...getRootProps()}>
      <input {...getInputProps()} />
      {
        isDragActive ?
          <p>Drop the files here ...</p> :
          <p>Drag 'n' drop some files here, or click to select files</p>
      }
    </DropZoneDiv>
  )
}

export default FileDropZone