<%inherit file="page-base.mako"/>

<%block name="toco">
    <div data-spy="affix" data-offset-top="60" data-offset-bottom="200" class="bs-sidebar">
        ##${ctx.get("toc")}
    </div>
</%block>

<dl class="dl-horizontal">
    <dt>SRFI</dt>
    <dd>${ctx.get("srfi-code")}</dd>

    <dt>Title</dt>
    <dd>${ctx.get("title")}</dd>

    <dt>Author</dt>
    <dd>${ctx.get("author")}</dd>

    <dt>Revision</dt>
    <dd><a href="${ctx.get('page')}/revisions">${ctx.get("version")}</a></dd>

    <dt>Status</dt>
    <dd>${ctx.get("status")}</dd>

    <dt>Created</dt>
    <dd>${ctx.get("created")}</dd>

    <dt>Last-Modified</dt>
    <dd>${ctx.get("updated")}</dd>
</dl>

<hr />

##${ctx.get("content")}<br />
