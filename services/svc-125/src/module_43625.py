"""Service module 43625: business logic, no crypto."""


def calculate_total_43625(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43625():
    return 'module 43625 handles orders and invoices'
