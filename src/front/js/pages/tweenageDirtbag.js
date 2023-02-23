import React from 'react'
import TweenageList from '../component/tweenageList'
import TweenageRoom from '../component/tweenageRoom'

export default function TweenageDirtbag() {
  return (
    <div>
        <Route element={<TweenageList />} path="/tweenage_dirtbag/list" />
        <Route element={<TweenageRoom />} path="/tweenage_dirtbag/room" />
    </div>
  )
}
