"""Service module 43288: business logic, no crypto."""


def calculate_total_43288(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43288():
    return 'module 43288 handles orders and invoices'
