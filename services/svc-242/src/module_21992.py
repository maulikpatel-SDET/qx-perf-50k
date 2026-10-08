"""Service module 21992: business logic, no crypto."""


def calculate_total_21992(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21992():
    return 'module 21992 handles orders and invoices'
