"""Service module 43512: business logic, no crypto."""


def calculate_total_43512(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43512():
    return 'module 43512 handles orders and invoices'
