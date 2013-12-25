<%inherit file="../base.mako"/>

<div class="container">
    <div class="row">
        <div class="col-md-12">
            <h1>${ctx.get('displayName')}</h1>
            <label>Email:</label>${ctx.get('verifiedEmail')}
        </div>
    </div>
</div>
