import React from 'react';
import '../static/css/style.css';

const ListOfRepos = props => {
    const {reposData} = props;
    const reposList = reposData.map(repo => {
        var data = ''
        if (repo.description){
            data = <div>
                        <div className='card-body'>
                                <p className="card-text">{repo.description}</p>
                        </div>
                        <div className='card-footer'>
                            <p className='text-muted'>{repo.language}</p>
                        </div>
                    </div>
        } else {
            data = <div className='card-body'>
                        <p className='text-muted'>{repo.language}</p>
                    </div>
        }
        return (
            <div key={repo.id}>
                <div className="col-lg-12mb-2 p-3" key={repo.title}>
                    <div className='card'>
                        <div className='card-header'>
                            <a href={repo.html_url} target="_blank" className="">{repo.name}</a>
                        </div>
                        {data}
                    </div>
                </div>
            </div>
        )
    });

    return (
        <div>
            {reposList}
        </div>
    )
};

export default ListOfRepos;