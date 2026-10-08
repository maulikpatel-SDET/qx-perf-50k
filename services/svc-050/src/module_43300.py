"""Service module 43300: business logic, no crypto."""


def calculate_total_43300(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43300():
    return 'module 43300 handles orders and invoices'
