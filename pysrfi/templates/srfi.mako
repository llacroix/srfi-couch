<%inherit file="page-base.mako"/>

<%block name="toco">
    <div data-spy="affix" data-offset-top="60" data-offset-bottom="200" class="bs-sidebar">
        ${toc|n}
    </div>
</%block>

<dl class="dl-horizontal">
    <dt>SRFI</dt>
    <dd>4</dd>

    <dt>Title</dt>
    <dd>${title}</dd>

    <dt>Author</dt>
    <dd>${author}</dd>

    <dt>Version</dt>
    <dd>${version}</dd>

    <dt>Last-Modified</dt>
    <dd>${date}</dd>

    <dt>Status</dt>
    <dd>final</dd>

    <dt>Created</dt>
    <dd>---</dd>
</dl>

<hr />

${content|n}<br />
