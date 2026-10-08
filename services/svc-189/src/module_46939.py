"""Service module 46939: business logic, no crypto."""


def calculate_total_46939(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46939():
    return 'module 46939 handles orders and invoices'
