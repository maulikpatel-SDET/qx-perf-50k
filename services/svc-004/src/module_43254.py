"""Service module 43254: business logic, no crypto."""


def calculate_total_43254(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43254():
    return 'module 43254 handles orders and invoices'
