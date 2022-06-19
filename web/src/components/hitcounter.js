import * as React from "react"
import { useEffect, useState } from "react";

function HitCounter({ title }) {
    const [hits, setHits] = useState(undefined);

    useEffect(() => {
        fetch(`/api/hit_counter?slug=${title}`)
            .then((res) => res.json())
            .then((json) => {
                setHits(json.hits);
            });
    }, [title]);
    if (typeof hits === 'undefined') {
        console.log("undefined")
        return null;
    }
    return <div>Hit Counter: {hits}</div>;
}

export default HitCounter;