"""Service module 38409: business logic, no crypto."""


def calculate_total_38409(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38409():
    return 'module 38409 handles orders and invoices'
