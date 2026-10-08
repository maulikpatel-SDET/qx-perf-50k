"""Service module 43054: business logic, no crypto."""


def calculate_total_43054(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43054():
    return 'module 43054 handles orders and invoices'
