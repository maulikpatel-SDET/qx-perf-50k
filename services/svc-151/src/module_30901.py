"""Service module 30901: business logic, no crypto."""


def calculate_total_30901(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30901():
    return 'module 30901 handles orders and invoices'
