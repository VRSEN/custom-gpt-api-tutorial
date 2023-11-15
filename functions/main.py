# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

from firebase_admin import initialize_app
from firebase_functions import https_fn
from google.analytics.data_v1beta import BetaAnalyticsDataClient, OrderBy
from google.analytics.data_v1beta.types import DateRange, Dimension, Metric

from schema import GA4QueryParams
from schema_example import Add2Numbers

initialize_app()

db_token = ""


@https_fn.on_request()
def query_ga4_data(req: https_fn.Request):
    token = req.headers.get("Authorization").split("Bearer ")[1]

    if token != db_token:
        return https_fn.Response("Unauthorized", status=401)

    analytics = BetaAnalyticsDataClient.from_service_account_file(
        "./custom-gpts-tutorial-c06142bfc81a.json"
    )

    property_id = 406502200

    print("Request", req.get_json())

    try:
        data: GA4QueryParams = GA4QueryParams(**req.get_json())

        request_body = {
            'property': f"properties/{property_id}",
            'date_ranges': [DateRange(**date_range.model_dump()) for date_range in data.date_ranges],
            'dimensions': [Dimension(**dimension.model_dump()) for dimension in data.dimensions],
            'metrics': [Metric(**metric.model_dump()) for metric in data.metrics],
            'order_bys': [OrderBy(**order_by.model_dump()) for order_by in data.order_bys],
            'limit': data.limit,
        }

        report = analytics.run_report(request=request_body)

        return {
            "data": str(report.rows),
        }
    except Exception as e:
        print("Analytics error: ", e)
        return {
            "error": str(e)
        }

@https_fn.on_request()
def add_2_numbers(req: https_fn.Request):
    token = req.headers.get("Authorization").split("Bearer ")[1]

    if token != db_token:
        return https_fn.Response("Unauthorized", status=401)

    try:
        data = Add2Numbers(**req.get_json())

        return {
            "data": data['number1'] + data['number2']
        }
    except Exception as e:
        print("Add 2 numbers error: ", e)
        return {
            "error": str(e)
        }
