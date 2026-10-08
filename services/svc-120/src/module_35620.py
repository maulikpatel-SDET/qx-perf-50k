"""Service module 35620: business logic, no crypto."""


def calculate_total_35620(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35620():
    return 'module 35620 handles orders and invoices'
