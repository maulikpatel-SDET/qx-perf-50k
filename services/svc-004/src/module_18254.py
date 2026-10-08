"""Service module 18254: business logic, no crypto."""


def calculate_total_18254(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18254():
    return 'module 18254 handles orders and invoices'
