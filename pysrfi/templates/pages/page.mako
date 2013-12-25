<%inherit file="../base.mako"/>

<%block name="title">
    Current user is ${current_user}
</%block>

${self.render_contents(ctx)}

<hr />

<div class="container">
    <div class="row">
        <div class="col-md-12">
            <span class="pull-right"><em>${ctx.get("@updated")}</em> by ${ctx.get("@author")}</span>
        </div>
    </div>
</div>
