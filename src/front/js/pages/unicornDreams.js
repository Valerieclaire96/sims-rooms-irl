import React from 'react'
import UnicornList from '../component/unicornList'
import UnicornRoom from '../component/unicornRoom'

export default function UnicronDreams() {
  return (
    <div>
        <Route element={<UnicornList />} path="/unicorn_dream/list" />
        <Route element={<UnicornRoom />} path="/unicorn_dream/room" />
    </div>
  )
}
