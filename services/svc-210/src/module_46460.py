"""Service module 46460: business logic, no crypto."""


def calculate_total_46460(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46460():
    return 'module 46460 handles orders and invoices'
