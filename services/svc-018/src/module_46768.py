"""Service module 46768: business logic, no crypto."""


def calculate_total_46768(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46768():
    return 'module 46768 handles orders and invoices'
