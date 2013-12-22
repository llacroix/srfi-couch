# SRFI Couch

# Abstract

Scheme Requests for Implementation has been designed a long time ago and
probably hasn't changed for many years. This site has for a goal to make
things more alive in the Scheme community.

SRFIs are the closest thing to python's PEPs for Scheme, they almost 
exclusively define libraries while the idea behind PEPs is much more general.

The requirements for the SRFI proposal process should be changed as they are
getting less relevant each year. The technology that we have now could probably
improve the way standards such as SRFI can get edited.

The requirements for the srfi proposal process can be found
[here](http://srfi.schemers.org/srfi-process.html#structure).

# How does this project can help improve things

The SRFI process requires all document to be written as HTML 3.2. We are in 
2013 and HTML5 what people are using nowadays. But even with that, I wouldn't
recommend any document to be written in HTML as HTML comes with styles.

After reading many SRFIs I noticed that each SRFI comes with different sets of
styles. Some comes with table of contents some don't.

For this reason, I propose to ditch the html completly as much as it is possible
and move on to some other file format that are style agnostic. Python community 
created its own format (Restructured Text). In the long run, I'd imagine the Scheme
community could instead use a subset of markdown that is more adapted to writing
srfi documents.

Each document can be downloaded as text file or being converted into any kind of
parser. Documents could be used to create PDF version or even get hosted on
different sites with new styles. A text file such as markdown is much more easily
editable than the current srfi documents.

Most srfi markup aren't even right. Take this small example:

    <p> some text
        more text...

    <p> A new paragraph
        more text...

    <ul><li> New list
        <li> New list element
        <li> More elements ...

    <p> A new paragraph

A smart html parser knows that paragraphs can't contain paragraphs and will
automatically close the open tags when it can't nest objects. Unfortunately
the processing of invalid tags might differ and could give really bad results.

A html page with bad markup is hard to parse and process correctly to automatically
modify them.

# Proposition

Save each document as markdown document, each new version creates a new document. 
We can easily track the state of documents in time. Draft and changes are going to be
dynamic. There is no need to setup or give server access. 

Each version could be accessible and there is little or no limit on how many revision 
a person can do. Each revision would be saved under the user who made the revision. This
way, it will be possible to track who made which changes to the document. In the end
I'd implement something that could probably look a lot like how Stackoverflow handle
questions edition.

Implementation file could be uploaded with the document and saved automatically
on the server.

It has to look nice and the used of Biwascheme could allow us to add an
interactive scheme REPL within the site. Scheme doesn't have to look old
because it's old.

