"""Service module 43093: business logic, no crypto."""


def calculate_total_43093(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43093():
    return 'module 43093 handles orders and invoices'
