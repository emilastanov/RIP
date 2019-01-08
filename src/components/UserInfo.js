import React from 'react';
import '../static/css/style.css';

const UserInfo = props => {
    const {userInfo} = props;
    const userInfoBlock = () => {
        console.log(userInfo);
        return (
            <div>
                <div className='row my-4'>
                    <div className="col-lg-6 col-md-6">
                        {userInfo.avatar_url && <img className='img-thumbnail avatar' src={userInfo.avatar_url} alt="Фото"/>}
                    </div>
                    <div className="col-lg-6 col-md-6">
                        <a href={userInfo.html_url} target="_blank" className="">{userInfo.login}</a>
                        <p>{userInfo.name}</p>
                        <p className='text-muted'>{userInfo.location}</p>
                        <p>{userInfo.bio}</p>
                        <div className="">
                            {userInfo.followers &&
                            <p style={{'padding': '0', 'margin': '0'}}><span className='text-muted'>Подписчики:</span> {userInfo.followers} </p>
                            }
                            {userInfo.following &&
                            <p style={{'padding': '0', 'margin': '0'}}><span className='text-muted'> Подписки:</span> {userInfo.following}</p>
                            }
                        </div>
                    </div>
                </div>
                <div className='text-center text-muted'>
                    {userInfo.public_repos &&
                    <p>Список репозиториев ({userInfo.public_repos})</p>
                    }
                </div>
            </div>
        )
    };

    return (
        <div>
            {userInfoBlock()}
        </div>
    )
};

export default UserInfo;