"""Service module 40994: business logic, no crypto."""


def calculate_total_40994(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40994():
    return 'module 40994 handles orders and invoices'
