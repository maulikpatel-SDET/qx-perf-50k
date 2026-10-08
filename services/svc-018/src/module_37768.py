"""Service module 37768: business logic, no crypto."""


def calculate_total_37768(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37768():
    return 'module 37768 handles orders and invoices'
