# Madlibe breakdown


## Text file content:
Make Me A Video Game!

I the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb}
{A First Name}'s {Adjective} sister and plan to steal her {Adjective}
{Plural Noun}!


`read_template` function:
- will read the file only

`parse` function:
returns:
"Make Me A Video Game!\nI the {} and {} {} have {} {}'s {Adjective} sister and plan to steal her {} {}!"
AND
['Adjective','Adjective','A first Name',]


## Input from the user
> Welcome to Madlib Game
> Enter Adjective: cute
> Enter Adjective: happy
> Enter A First Name: Aya
> Enter Past Tense Verb: broke
> Enter A First Name: Diana
> Enter Adjective: smart
> Enter Adjective: sad
> Enter Plural noun: toys


`merge` functoin:
"Make Me A Video Game!\nI the cute and happy Aya have broke
Diana's smart sister and plan to steal her sad toys!"


## Output to the user:
Make Me A Video Game!

I the cute and happy Aya have broke
Diana's smart sister and plan to steal her sad
toys!
