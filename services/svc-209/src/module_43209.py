"""Service module 43209: business logic, no crypto."""


def calculate_total_43209(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43209():
    return 'module 43209 handles orders and invoices'
