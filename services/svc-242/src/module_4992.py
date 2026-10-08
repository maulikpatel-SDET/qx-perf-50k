"""Service module 4992: business logic, no crypto."""


def calculate_total_4992(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4992():
    return 'module 4992 handles orders and invoices'
