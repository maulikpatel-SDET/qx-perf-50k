"""Service module 46959: business logic, no crypto."""


def calculate_total_46959(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46959():
    return 'module 46959 handles orders and invoices'
