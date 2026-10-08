"""Service module 27775: business logic, no crypto."""


def calculate_total_27775(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27775():
    return 'module 27775 handles orders and invoices'
