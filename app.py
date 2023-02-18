from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'JS Tag Validator!'


@app.route('/js_tag/<placement>/<campaign>')
def js_validator(placement, campaign):
    query_params = request.args.to_dict()
    js_tag = f'<ins class="dcmads" style="display:inline-block;width:{query_params["width"]};height:{query_params["height"]}" data-dcm-placement="{placement}/{campaign}" data-dcm-rendering-mode="script" data-dcm-https-only data-dcm-gdpr-applies="gdpr=${{GDPR}}" data-dcm-gdpr-consent="gdpr_consent=${{GDPR_CONSENT_755}}" data-dcm-addtl-consent="addtl_consent=${{ADDTL_CONSENT}}" data-dcm-ltd="false" data-dcm-resettable-device-id="" data-dcm-app-id=""> <script src="https://www.googletagservices.com/dcm/dcmads.js"></script> </ins>'
    raw_html_content = r'<!DOCTYPE html><html><head><title>DCM Ad Example</title></head><body>{js_tag}</body></html>'
    html_content = raw_html_content.replace('{js_tag}', js_tag)
    return html_content


if __name__ == '__main__':
    app.run()
