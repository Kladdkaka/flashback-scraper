import styled from "styled-components/macro";
import React, {useCallback} from "react";


function Thread({entries}) {
  return (
    <div>
      {entries.map((entry, index) => (
        <Post key={index} index={index} entry={entry}/>
      ))}
    </div>
  )
}

const PostDiv = styled.div`
  width: 100%;
  margin: -1px 0 0 0;
  border-bottom: 1px solid #e3e3e3;
  background: #eff0f1;
`

const PostHeading = styled.div`
  background: #ccc;
  padding: 5px;
  color: #333;
`


const PostBody = styled.div`
  background: #eff0f1;
  display: table;
  border-collapse: collapse;
  width: 100%;
`

const PostRow = styled.div`
  height: 100%;
  display: table-row;
`

const PostCol = styled.div`
  display: table-cell;
  float: none;
  vertical-align: top;
`

const PostColLeft = styled(PostCol)`
  background: #e3e3e3;
  width: 140px;
  vertical-align: top;
  padding: 5px;
`

const PostColRight = styled(PostCol)`
  font-family: 'San Francisco','SNFS Display',BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol";
  font-size: 13px;
  line-height: 17.7px;
  background: #eff0f1;
  padding: 5px;
`


function Post({index, entry}) {
  return (
    <PostDiv key={index}>
      <PostHeading>
        2021-09-09, 23:59
        <div style={{float: 'right'}}>
          &nbsp;
          #<strong>{index}</strong>
        </div>
      </PostHeading>

      <PostBody className="post-body">
        <PostRow className="post-row">
          <PostColLeft className="post-col post-left">
            <div className="post-user">
              <a className="post-user-username" style={{
                fontWeight: 700,
                textDecoration: 'underline',
                color: '#000'
              }}>{entry.username}</a>

              <div className="post-user-title">{entry.user_title}</div>


              <a className="post-user-avatar">
                <img src={entry.avatar_url}/>
              </a>

              <div className="post-user-info" style={{marginTop: '5px'}}>
                {entry.user_info}
              </div>
            </div>

          </PostColLeft>

          <PostColRight className="post-col post-right">
            <div className="post_message" style={{wordBreak: 'break-word'}}>
              {entry.message}
            </div>
          </PostColRight>
        </PostRow>
      </PostBody>
    </PostDiv>
  )
}

export default Thread