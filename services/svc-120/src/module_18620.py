"""Service module 18620: business logic, no crypto."""


def calculate_total_18620(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18620():
    return 'module 18620 handles orders and invoices'
