# Crusoe
**category :** reverse,
**points :** 60,
**solves :** 87.

## Description :
The Spaniard owes Crusoe one, would he help him to escape his island?

Update: It seems that there are multiple acceptable strings that generate the flag.crusoe. Get the flag from the remote server. Check your strings with this server.
```
nc <ip> <port>
```

## Solution :
There are 2 files in here,
1. A binary file - crusoe.
2. A text file - flag.crusoe.

We can understand that crusoe might be a language like english in which our flag was encoded and we know the encoded form of flag (flag.crusoe) and the binary (crusoe) which did that.

By experimenting with the binary we can find that,
* for every single alpha char [A-Za-z] - 2 pictograms were printed.
```
$ ./crusoe 
q
                  
  _()       ()    
 []/^     | /^    
  <>[      <>[    

```
* for n alpha chars [A-Za-z]{n} - (n+1) pictograms were printed.
```
qw
             <>            
  _()       /)_      ()    
 []/^       ^^[]   | /^    
  <>[       ][      <>[

```
* And (n+1)th pictogram feels like terminating char as it is present all the time.
* for special characters (-+,).. - nothing was printed.
* for every digit - 3 pictograns were printed.
```
1
             []            
  _()       ()|      ()    
 []^\       /^     | /^    
   ][ <> <> ][      <>[    

```
Now the solution is simply to map the pictograms to the appropriate chars in the flag.crusoe. (there were multiple multiple answers for this)

```
$ cat flag.crusoe
             <>              []       [] <>                     <> []   
  _()       /)       ()      |()_     |()/     _()      _()      \()|   
 []/^       ^\       /\       ^^[]     ^^     []^\     []/^       ^^    
  <>[       ][ <> <> ][ <>    ][       ][       ][ <>   <>[       ][    

  []       [] <>               <>    <> []             <>               
  |()_     |()/      ()       /)      \()|      ()_     \()       ()    
   ^^[]     ^^       /\       ^\       ^^       /^[]     ^\       /\    
   ][       ][    <> ][ <>    ][ <>    ][    <> ][       ][ <> <> ][ <> 

  <>               <> []                <>                         []   
   (\       ()_     \()|     _()       /)_      ()_     _()       ()|   
   /^       /^[]     ^^     []^\       ^^[]     /^[]   []^\       /^    
<> ][    <> ][       ][       ][ <>    ][    <> ][       ][ <> <> ][    

           <>       <>                <>       []       <>      <>      
  _()       (\       (\       ()_      (\      |()_      (\      \()    
 []^\       ^\       /^       /^[]     ^\       ^^[]     ^\       ^\    
   ][ <>    ]<>   <> ][    <> ][       ]<>      ][       ]<>      ][ <> 

 <> []       <>     []                <>                                
  \()|      /)      |()_      ()       (\      _()       ()_      ()_   
   ^^       ^\       ^^[]     /\       /^     []/^     | ^^[]   | ^^[]  
   ][       ][ <>    ][    <> ][ <> <> ][      <>[      [][      [][    

  <>                <>       <>      <>                         <>      
   (\      _()       (\       (\      \()_      ()_     _()      \()    
   /^     []^\       ^\       /^       ^^[]   | ^^[]   []^\       ^\    
<> ][       ][ <>    ]<>   <> ][       ][      [][       ][ <>    ][ <> 

 <> []                                  <>                []            
  \()|     _()      _()      _()       /)      _()       ()|      ()    
   ^^     []^\     []^\     []^\       /^     []^\       /^       /\    
   ][       ][ <>    ][ <>    ][ <>   <>[       ][ <> <> ][    <> ][ <> 

           [] <>    <>       <>         <>                []            
   ()_     |()/      (\       (\       /)      _()       ()|      ()    
 | ^^[]     ^^       /^       ^\       ^\     []^\       /^     | /^    
  [][       ][    <> ][       ]<>      ][ <>    ][ <> <> ][      <>[

```

Below are few of the answers which we can feed to get the flag.
* "qxnjubqtjunxtmdnhmtbwmbkbghmgjgdtxjnhqzzhbghyzbdtbbbebknzuhgxbk"
```
$ diff <(printf "qxnjubqtjunxtmdnhmtbwmbkbghmgjgdtxjnhqzzhbghyzbdtbbbebknzuhgxbk" | ./crusoe) <(cat flag.crusoe); echo $?
0
```
* "cxnjubctjunxtmdnhmtbwmbkbghmgjgdtxjnhczzhbghyzbdtbbbebknzuhgxbk" (c & q represent same).

Output from flag checker :
```
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+       ..:: Crusoe flag checker ::..       +
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
| Please input your right answer for Crusoe task: 
qxnjubqtjunxtmdnhmtbwmbkbghmgjgdtxjnhqzzhbghyzbdtbbbebknzuhgxbk
Congrats! this is the flag: ASIS{cRuS03_10V3__0bFu5c4T3d__c0COnu75!!}
```

# Flag :
ASIS{cRuS03_10V3__0bFu5c4T3d__c0COnu75!!}
