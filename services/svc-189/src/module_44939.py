"""Service module 44939: business logic, no crypto."""


def calculate_total_44939(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44939():
    return 'module 44939 handles orders and invoices'
