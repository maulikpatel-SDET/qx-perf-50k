"""Service module 43679: business logic, no crypto."""


def calculate_total_43679(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43679():
    return 'module 43679 handles orders and invoices'
