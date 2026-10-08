"""Service module 10809: business logic, no crypto."""


def calculate_total_10809(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10809():
    return 'module 10809 handles orders and invoices'
