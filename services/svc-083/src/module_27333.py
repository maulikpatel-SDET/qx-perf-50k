"""Service module 27333: business logic, no crypto."""


def calculate_total_27333(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27333():
    return 'module 27333 handles orders and invoices'
